[![version](https://hack.conference.ioer.info/version.svg)][static-gl-url] [![pipeline](https://hack.conference.ioer.info/pipeline.svg)][static-gl-url] [![doi](https://hack.conference.ioer.info/doi.svg)][doi-url]

# Sustainability Transformation Hackathon (IOER Conference 2026)

Welcome to the collaborative workspace for the **Conference Hack**, a dedicated contribution format (F5) of the **4th IOER Conference "Space & Transformation"**.

This repository hosts the source code and notebooks for the living **Jupyter Book**, available at https://hack.conference.ioer.info/. 

Unlike traditional hackathons, this project is an **asynchronous, collaborative data challenge**. Participants contribute code, visualizations, and workflows to this repository, which are then compiled into a citable **ioerDATA publication** representing the collective output of the conference format.

All internal collaboration and continuous integration/deployment (CI & CD) takes place in [this Gitlab repository](https://gitlab.hrz.tu-chemnitz.de/ioer/fdz/training/hackathon-ioer-conference-2026/).

For public collaboration, we set up a [mirror on Github](https://github.com/ioer-dresden/ioer-conference-2026-hackathon).

## TL;DR: How to Contribute

The workflow for participants and maintainers is as follows:

1.  **Code:** Edit existing notebooks or add new ones (`*.ipynb` files) in the `notebooks/` directory.
2.  **Submit:** Commit changes (preferably on a separate branch or fork) and create a **Pull Request**.
3.  **Build:** The CI/CD pipeline converts notebooks to Markdown and builds the Jupyter Book.
4.  **Publish:** The updated book is deployed automatically:
    *   **Staging (Review):** https://stag.hack.conference.ioer.info/
    *   **Production (Final):** https://hack.conference.ioer.info/

 ```mermaid 
 %%{init: { 'theme':'forest', 'securityLevel': 'loose', 'sequence': {'useMaxWidth':false} } }%%
 flowchart LR;
    notebooks/01_introduction.ipynb-->01_introduction.md-->HTML-->Gitlab-CI-->Webserver-->'hack.conference.ioer.info'
 ```

See the [Contribution Documentation](https://hack.conference.ioer.info/CONTRIBUTING.html) for a detailed walkthrough of the collaboration process.

## Participants & Developers

This infrastructure allows you to focus on the content (Sustainability, Digitalisation, Spatial Analysis) without worrying about web hosting.

*   **Cloud Execution:** You can run the Notebooks directly in your browser via the **Jupyter4NFDI Hub** (link available in the top menu bar of the book).
*   **Local Execution:** If you prefer working locally, please refer to the instructions for the IOER FDZ [Carto-Lab Docker](https://cartolab.fdz.ioer.info/), provided in the [Setup Chapter][1].
*   **Versioning:** This repository is versioned with [python-semantic-release](https://python-semantic-release.readthedocs.io/en/latest/).

For a step-by-step guide on how to make your first Pull Request, see the [Contributing Section](https://hack.conference.ioer.info/CONTRIBUTING.html).


[1]: https://hack.conference.ioer.info/notebooks/101_jupyter_notebooks.html#carto-lab-docker
[static-gl-url]: https://gitlab.hrz.tu-chemnitz.de/ioer/fdz/training/hackathon-ioer-conference-2026
[doi-url]: https://tbd
