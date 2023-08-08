## Description

A automated way to create project's document for Ineuron Portal Projects.

## 🤖 Automate Project Documentation with `PyPDF2`

- [x] Make wholesome documents for ML Projects using `ChatGPT` made some correction to it.
- [x] Also add **photos of diagrams** which shows the particular process of the project.
- [x] **Add placeholder** `**/*[[placeholder_name]]*/**` where you think that it vary projects to projects.
- [ ] Write the document in Markdown format and read the the Markdown file make changes to it (easier than PDF files).
- [x] Use `PyPDF2` read the PDF documents and get all the placeholders using `regex`.
- [x] **Create functions** which is used to fill these placeholder.
- [ ] Export the Markdown as PDF file using some Python library.

## TODO

- [x] Ask ChatGPT and Bard: Create a function which returns Table of Contents by reading a markdown file. Function takes md file path as parameter.
- [x] Create a function which replace the patterns from markdown file with it value. Get the patterns' value from yaml file. Function takes markdown file path and yaml file path.
- [ ] Remove the numbering from headers.
- [x] Update the pattern as `{{}}` instead of `/*[[]]*/`.
- [ ] As you make doc the `{[ProjectName]}` get placed in `{[TableOfContents]}` instead of its value.
