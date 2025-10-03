const fs = require("fs");
const path = require("path");

/** @type {import('@docusaurus/types').PluginModule} */
module.exports = function (context, options) {
  return {
    name: "dynamic-pages",

    async loadContent() {
      const leaksDir = path.join(context.siteDir, "leaks");
      const docsDir = path.join(context.siteDir, "docs");

      if (!fs.existsSync(docsDir)) {
        fs.mkdirSync(docsDir, { recursive: true });
      }

      const promptFolders = fs
        .readdirSync(leaksDir, { withFileTypes: true })
        .filter(
          (/** @type {fs.Dirent} */ dirent) =>
            dirent.isDirectory() && !dirent.name.startsWith(".")
        )
        .map((/** @type {fs.Dirent} */ dirent) => dirent.name);

      const generatedPages = [];
      for (const folderName of promptFolders) {
        const folderPath = path.join(leaksDir, folderName);
        const archivedPath = path.join(folderPath, "archived");

        const hasArchived =
          fs.existsSync(archivedPath) &&
          fs
            .readdirSync(archivedPath, { withFileTypes: true })
            .some(
              (/** @type {fs.Dirent} */ dirent) =>
                dirent.isFile() && !dirent.name.startsWith(".")
            );

        const files = fs
          .readdirSync(folderPath, { withFileTypes: true })
          .filter(
            (/** @type {fs.Dirent} */ dirent) =>
              dirent.isFile() && !dirent.name.startsWith(".")
          )
          .map((/** @type {fs.Dirent} */ dirent) => ({
            name: dirent.name,
            path: path.join(folderPath, dirent.name),
          }))
          .sort((a, b) => b.name.localeCompare(a.name));

        if (files.length === 0) continue;

        let mdxContent;
        if (hasArchived) {
          const archivedFiles = fs
            .readdirSync(archivedPath, { withFileTypes: true })
            .filter(
              (/** @type {fs.Dirent} */ dirent) =>
                dirent.isFile() && !dirent.name.startsWith(".")
            )
            .map((/** @type {fs.Dirent} */ dirent) => ({
              name: dirent.name,
              path: path.join(archivedPath, dirent.name),
            }))
            .sort((a, b) => b.name.localeCompare(a.name));

          mdxContent = generateMDXContent(folderName, files, docsDir, {
            additionalTabs: [
              {
                value: "archived",
                label: "archived",
                files: archivedFiles,
              },
            ],
          });
        } else {
          mdxContent = generateMDXContent(folderName, files, docsDir);
        }

        const mdxFileName = `${folderName}.mdx`;
        const mdxFilePath = path.join(docsDir, mdxFileName);
        fs.writeFileSync(mdxFilePath, mdxContent, "utf8");

        generatedPages.push({
          folderName,
          fileName: mdxFileName,
          fileCount: files.length,
          hasArchived: hasArchived || false,
        });
      }

      return generatedPages;
    },

    async contentLoaded({ content, actions }) {
      const { setGlobalData } = actions;

      setGlobalData({
        generatedPages: content,
      });
    },
  };
};

/**
 * @param {string} folderName
 * @param {{name: string, path: string}[]} files
 * @param {string} docsDir
 * @param {{
 *   title?: string,
 *   description?: string,
 *   primaryTabValue?: string,
 *   primaryTabLabel?: string,
 *   additionalTabs?: Array<{value: string, label: string, files: {name: string, path: string}[]}>
 * }} options - Configuration options
 * @returns {string}
 */
function generateMDXContent(folderName, files, docsDir, options = {}) {
  const {
    title = folderName,
    description = `${folderName} Prompt`,
    primaryTabValue = "latest",
    primaryTabLabel = "latest",
    additionalTabs = [],
  } = options;

  /**
   * @param {{name: string, path: string}[]} fileList
   * @param {string} tabSuffix
   * @returns {string}
   */
  const generateTabs = (fileList, tabSuffix = "") => {
    return fileList
      .map((file) => {
        const fileName = file.name;
        const fileNameKebab = fileName
          .split(".")[0]
          .toLowerCase()
          .replace(/\s+/g, "-")
          .replace(/_/g, " ");
        const extension = path.extname(fileName).slice(1);
        const language = getLanguageFromExtension(extension);

        return `        <TabItem value="${fileNameKebab}${tabSuffix}" label="${fileNameKebab}" attributes={{ className: "tabs__vertical" }}>
          <CodeBlock language="${language}">{require('!!raw-loader!${path.relative(docsDir, file.path)}').default}</CodeBlock>
        </TabItem>`;
      })
      .join("\n");
  };

  const primaryTabs = generateTabs(files);
  let allTabs = [
    `    <TabItem value="${primaryTabValue}" label="${primaryTabLabel}">
      <Tabs queryString="secondary">
${primaryTabs}
      </Tabs>
    </TabItem>`,
  ];

  additionalTabs.forEach((tab) => {
    if (tab.files && tab.files.length > 0) {
      const tabsContent = generateTabs(tab.files, `-${tab.value}`);
      allTabs.push(`    <TabItem value="${tab.value}" label="${tab.label}">
      <Tabs queryString="secondary">
${tabsContent}
      </Tabs>
    </TabItem>`);
    }
  });

  return `---
title: ${title}
description: ${description}
hide_table_of_contents: true
---

import CodeBlock from "@theme/CodeBlock";
import TabItem from "@theme/TabItem";
import Tabs from "@theme/Tabs";

<Tabs queryString="primary">
${allTabs.join("\n")}
</Tabs>`;
}

/**
 * @param {string} extension
 * @returns {string}
 */
function getLanguageFromExtension(extension) {
  /** @type {Record<string, string>} */
  const languageMap = {
    md: "markdown",
    js: "javascript",
    ts: "typescript",
    py: "python",
    json: "json",
    yaml: "yaml",
    yml: "yaml",
  };

  return languageMap[extension] || "text";
}
