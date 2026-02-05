---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.17.3
  kernelspec:
    display_name: worker_env
    language: python
    name: worker_env
---

<!-- #region editable=true slideshow={"slide_type": ""} -->
# Theory chapters 
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
```{admonition} Why we are doing this? What is the motivation of these training materials?
:class: tip
At the IOER we are committed to the principles of open, reproducible, accessible and transparent science. To this end, documenting and sharing the code we use to process data and generate figures and results is critical. By using tools such as [JupyterLab](https://jupyter.org/), we enable others to reproduce our results and workflows. We also use this framework ([Jupyter Book](https://jupyterbook.org/en/stable/intro.html)) to document our own application programming interfaces (APIs), so that others (you!) can copy code snippets to access our data.

**A Core Resource:** Much of the foundational knowledge for research data management (RDM) in biodiversity is comprehensively covered in the **NFDI4Biodiversity Self-Study Unit: Research Data Management for Biodiversity Data** by {cite:t}`fischer_2023_10377868`. We highly recommend consulting this unit for in-depth explanations, particularly on topics like Data Management Plans (DMPs), the data life cycle, and detailed considerations for data collection, preservation, and sharing. The following sections provide a summary of key concepts, often drawing upon or aligning with this excellent resource.
```
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
```{admonition} Summary
:class: note
- The **FAIR principles** provide guidelines to make data **Findable**, **Accessible**, **Interoperable**, and **Reusable**, ensuring data is well-organized, machine-readable, and optimized for reuse across disciplines.
- **Data provenance** refers to the documentation of the origin, history, and data processing.
- **Metadata** is information that describes and organizes data, enabling easier discovery and use.
- A **license** defines the permissions, restrictions, and terms under which data or software can be used, shared, and modified.
```
<!-- #endregion -->

<!-- #region slideshow={"slide_type": ""} editable=true -->
## **FAIR principles**

The **F**indable **A**cessible **I**nteroperable **R**eusable (**FAIR**) principles *({cite:alp}`wilkinson_fair_2016`)* are the culmination of more than 20 years of agreements and discussions within industry and academia to address the critical issue of managing the most crucial asset of any research activities, namely the **DATA**.

The FAIR principles listed below follow the [Go FAIR initiative](https://www.go-fair.org/fair-principles/)

**Findable**
The first step in (re)using data is to find them. Metadata and data should be easy for both humans and computers to find. Machine-readable metadata plays a crucial role in enabling the automatic discovery of datasets and services. 

- **[F1](https://www.go-fair.org/fair-principles/f1-meta-data-assigned-globally-unique-persistent-identifiers/)** (Meta)data are assigned a globally unique and persistent identifier

- **[F2](https://www.go-fair.org/fair-principles/f2-data-described-rich-metadata/)** Data are described with rich metadata (defined by R1 below)

- **[F3](https://www.go-fair.org/fair-principles/f3-metadata-clearly-explicitly-include-identifier-data-describe/)** (Meta)data clearly and explicitly include the identifier of the data they describe

- **[F4](https://www.go-fair.org/fair-principles/f4-metadata-registered-indexed-searchable-resource/)** (Meta)data are registered or indexed in a searchable resource** F1: (Meta) data are assigned globally unique and persistent identifiers

**Accessible**
Once users have found the required data, they need to understand how to access it. This involves determining whether the data is openly available or requires authentication and authorization, such as login credentials. Users must know the methods for retrieving the data, whether through direct downloads, APIs, or repositories. Finally, it is essential to consider any restrictions or conditions on access.

- **[A1](https://www.go-fair.org/fair-principles/metadata-retrievable-identifier-standardised-communication-protocol/)** (Meta)data are retrievable by their identifier using a standardised communications protocol
    - **[A1.1](https://www.go-fair.org/fair-principles/a1-1-protocol-open-free-universally-implementable/).** The protocol is open, free and universally implementable
    - **[A1.2](https://www.go-fair.org/fair-principles/a1-2-protocol-allows-authentication-authorisation-required/).** The protocol allows for an authentication and authorisation procedure where necessary
- **[A2](https://www.go-fair.org/fair-principles/a2-metadata-accessible-even-data-no-longer-available/)** (Meta)data is accessible, even when the data are no longer available

**Interoperable**
The data usually needs to be integrated with other data. In addition, the data needs to interoperate with applications or workflows for analysis, storage, and processing.

- **[I1](https://www.go-fair.org/fair-principles/i1-metadata-use-formal-accessible-shared-broadly-applicable-language-knowledge-representation/)** (Meta)data use a formal, accessible, shared, and broadly applicable language for knowledge representation.

- **[I2](https://www.go-fair.org/fair-principles/i2-metadata-use-vocabularies-follow-fair-principles/)** (Meta)data use vocabularies that follow FAIR principles

- **[I3](https://www.go-fair.org/fair-principles/i3-metadata-include-qualified-references-metadata/)** (Meta)data include qualified references to other (meta)data

**Reusable**
The ultimate goal of FAIR is to optimise data reuse. To achieve this, metadata and data should be well-described to be replicated and/or combined in different settings.

- **[R1](https://www.go-fair.org/fair-principles/r1-metadata-richly-described-plurality-accurate-relevant-attributes/)** (Meta)data are richly described with accurate and relevant attributes.
    - **[R1.1](https://www.go-fair.org/fair-principles/r1-1-metadata-released-clear-accessible-data-usage-license/)** (Meta)data are released with a clear and accessible data usage license.
    - **[R1.2](https://www.go-fair.org/fair-principles/r1-2-metadata-associated-detailed-provenance/)** (Meta)data are associated with detailed provenance.
    - **[R1.3](https://www.go-fair.org/fair-principles/r1-3-metadata-meet-domain-relevant-community-standards/)** (Meta)data meet domain-relevant community standards.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": ""} editable=true -->
### **CARE Principles**

Complementing FAIR, the **CARE** Principles for Indigenous Data Governance (**C**ollective Benefit, **A**uthority to Control, **R**esponsibility, and **E**thics) were introduced by the Global Indigenous Data Alliance (GIDA) to address ethical concerns related to indigenous data *({cite:alp}`rizzolli_care_2022`)*. They emphasize the rights of Indigenous Peoples concerning their data, including information about their language, customs, and territories, and are increasingly relevant in biodiversity research involving traditional knowledge or resources from indigenous lands.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": ""} editable=true -->
## **Data Provenance** 
In scientific research, ensuring reproducibility remains a cornerstone of the scientific method. Reproducibility allows other researchers to verify findings by following the same methodology, reanalyzing data, and obtaining consistent results. In Data Science, it is fundamental to provide **transparent documentation, well-structured metadata, standardized workflows, and detailed <mark>provenance tracking</mark>** to capture every step of data processing and analysis. 
Unlike workflows, which serve as structured guidelines, **provenance** functions more like a detailed logbook by systematically recording every step to generate a specific result. This allows researchers to trace, review, and even replicate the exact process that led to a particular outcome, ensuring its validity ({cite:alp}`henzen_provenance_2013`).

For example, in typical geoscience research, provenance can include the:

- **Data source:** raw measurements, original vector and raster data, ground control data
- **Pre-processing Methods:** Reprojection of the geodata; Clipping the dataset to the bounds of a specific study area; Data cleaning (e.g., removing clouds or irrelevant features)
- **Data processing and analysis** Transformations applied include filtering, aggregation, resampling, joining, and/or model design with relative statistical analysis.
- **Model or statical parameters** with relative functions and code used in computations
- **The final output** and how it was generated 
  
`````{tip}
:class: tip
**A Jupyter Notebook** is an excellent tool for maintaining provenance in computational research. It records the entire workflow and provides a detailed logbook of all the data processing and analysis steps. Moreover, a Juper Notebook allows easy annotations to describe each step, improving clarity and documentation.


`````
<!-- #endregion -->

<!-- #region slideshow={"slide_type": ""} editable=true -->
## **Metadata (MD):** *"Data About Data"*

Metadata (MD) is often described as "data about data." It provides <mark>**structured information**</mark> about research data, enabling better organization, discovery, and context of datasets.  

### Why Is Metadata Important?

Metadata plays a crucial role for:  
- **Enhancing discoverability:** Well-documented metadata allows researchers to find relevant datasets quickly (*e.g. by using keywords in their search*).  
- **Ensuring Data Interoperability:** Standardized metadata enhances searchability and data integration by providing consistent descriptors (*e.g., using controlled vocabularies and standardized keywords for geospatial data*). It also facilitates the **collection and processing** of datasets across different platforms (*e.g. in the case of geospatial data, by adopting Open Geospatial Consortium (OGC) standard services (such as WMS, WFS, or WCS) allows seamless data retrieval and processing across various software and systems, including R, Python, QGIS, ArcGIS, and web-based GIS applications*). By ensuring metadata consistency (*e.g., uniformly defining coordinate reference systems, spatial extent, and thematic attributes*), interoperability is significantly improved, enabling researchers and analysts to integrate datasets from diverse sources efficiently.
- **Improving data reproducibility:** By providing details about how data was collected and processed (*e.g., by adding related links to the original data source, pre-processing algorithms, analysis-ready data, post-processing algorithms, replication packages and any related documentation such as data or software description article*).  
- **Facilitating long-term data usability and fit for purpose:** Metadata includes essential details such as data format, provenance/lineage, licensing, and links to other resources supporting research data's long-term sustainability and usability.  
- **Promoting proper Attribution, Credits, and Citations:** Metadata elements like Creator and License ensure creators hold copyright and can, therefore, be appropriately credited for their work while defining the usage condition for sharing and reusability.  

### What Does “Structured Metadata” Mean?  

Metadata follows a defined format. Standards are classified into:

- **General-Purpose Metadata Standards:** Broadly applicable (e.g., [DataCite Schema](https://doi.org/10.14454/mzv1-5b55), Dublin Core).
- **Domain-Specific Metadata Standards:** Tailored to fields (e.g., [ISO 19115](https://www.iso.org/standard/53798.html) for geodata; ABCD, Darwin Core, EML for biodiversity data; see {cite:t}`fischer_2023_10377868`, Sec. 4.3.2.4 for more examples and resources like FAIRsharing.org to find standards).

Common metadata elements (largely based on DataCite) include:  
- **Title:** The name of the dataset or research work.  
- **Creator:** The individual(s) or organization(s) responsible for generating the data.  
- **Abstract:** A summary of the dataset’s content and purpose.  
- **Keywords:** Terms that help categorize and index the data for easier retrieval.  
- **Format:** The file type or structure of the dataset (e.g., CSV, PDF, XML).  
- **Subject:** The broader topic or discipline related to the data.  
- **Persistent Identifier (PID):** A unique identifier (such as a DOI) ensures the dataset remains accessible over time.  
- **License:** The terms of use specifying how the data can be shared and reused.  
- **Provenance/Lineage:** Information on the origin and history of the dataset, including how it was created and modified.  

[<mark>**The ISO 19115:** </mark> Is a <mark>**domain-specific**</mark> metadata standard tailored specifically for **geodata**](https://www.iso.org/standard/53798.html), providing  further and extensive details on spatial, temporal, and thematic aspects of datasets such as:

- **Spatial Reference Information:** Coordinate Reference System (CRS), Projection details, Spatial resolution (scale, ground sampling distance)
- **Temporal Extent:** Period covered by the data, Frequency of updates (e.g., daily, annually)
- **Detailed Lineage and Data Provenance:** Source data origin (e.g., satellite imagery, field surveys), Data processing history (e.g., transformations, filtering, aggregation), Quality control procedures applied
- **Data Quality:** Positional accuracy (spatial precision), Logical consistency (topological and attribute correctness), Completeness (missing data, coverage gaps)
- **Geospatial Feature and Attribute Information:** Vector feature types (e.g., points, lines, polygons), Raster properties (resolution, pixel size, band information), Thematic classification (e.g., land cover categories)
- **Geospatial Services:** Web services (e.g., WMS, WFS, WCS from OGC)

Please [refer to the user guide of the National Agricultural Library (NAL)](https://geodata.nal.usda.gov/geonetwork/doc/geodata/NAL_UserGuide/19115_content/index.html) of the United States for a better explanation of the ISO 19115 metadata elements. 

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
### Controlled Vocabularies and Authority Files

To ensure consistency and machine-interpretability, metadata should use **controlled vocabularies** (predefined terms, thesauri like AGROVOC, or ontologies like ENVO) and **authority files** (standardized names/identifiers for entities like people via ORCID, organizations via ROR, or places via GeoNames). See {cite:t}`fischer_2023_10377868` Sec. 4.3.2.5 for details and resources like BARTOC or the GFBio Terminology Service).
<!-- #endregion -->

<!-- #region slideshow={"slide_type": ""} editable=true -->
## Intellectual Property and Licence

**Intellectual Property (IP)** refers to creations of the mind. **Intellectual Property Rights (IPR)**, like copyright, protect these creations. A **license** specifies conditions for access, modification, or sharing. (See {cite:alp}`fischer_2023_10377868` Sec. 7.2.5 for an in-depth guide).

```{admonition} Prefer CC0 or CC BY
:class: warning
IOER FDZ recommends open and specific licenses for spatial data. Internationally, [Creative Commons (CC) licenses](https://creativecommons.org/share-your-work/cclicenses/) are common. For Germany, [GOVDATA licenses](https://www.govdata.de/informationen/lizenzen) are recommended.
{cite:t}`fischer_2023_10377868` (Sec. 7.2.5) similarly advise CC0 or CC BY for creative content, warning against ND (NoDerivatives) and NC (NonCommercial) due to ambiguities that hinder reuse. For databases, Open Data Commons (ODC-PDDL, ODC-BY) or CC BY 4.0 are suitable. Raw data and metadata, often not copyrightable, can be marked with CC0 or a Public Domain Mark.
```

For software, use specific open-source licenses like GPL, MIT, or MPL, not CC licenses.

 ```{admonition} Tip
:class: hint
Not sure, which license you should choose? This [license chooser](https://chooser-beta.creativecommons.org/) helps you to find the appropriate license. 
```
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
### Selected International Creative Commons Licenses

| **License** | **Icon** | **License URL** | **SPDX link** |   Comment              |
|----------------------|----------|------------------------|------------------------|---------|
| CC0                  | ![](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg) | [CC0](https://creativecommons.org/publicdomain/zero/1.0/) | [SPDX](https://spdx.org/licenses/CC0-1.0.html)       | |
| CC-BY-4.0            | ![](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by.svg) | [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)      | [SPDX](https://spdx.org/licenses/CC-BY-4.0.html)      |  *IOER-FDZ default* |
| CC-BY-SA-4.0         | ![](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-sa.svg) | [CC-BY-SA-4.0](https://creativecommons.org/licenses/by-sa/4.0/)   | [SPDX](https://spdx.org/licenses/CC-BY-SA-4.0.html)   |
| CC-BY-NC-4.0         | ![](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-nc.svg) | [CC-BY-NC-4.0](https://creativecommons.org/licenses/by-nc/4.0/)   | [SPDX](https://spdx.org/licenses/CC0-1.0.html)       | *Use with caution* |
| CC-BY-ND-4.0         | ![](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-nd.svg) | [CC-BY-ND-4.0](https://creativecommons.org/licenses/by-nd/4.0/)   | [SPDX](https://spdx.org/licenses/CC-BY-ND-4.0.html)   | *Use with caution* |
| CC-BY-NC-SA-4.0      | ![](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-nc-sa.svg) | [CC-BY-NC-SA-4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) | [SPDX](https://spdx.org/licenses/CC-BY-NC-SA-4.0.html) | *Use with caution* |
| CC-BY-NC-ND-4.0      | ![](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-nc-nd.svg) | [CC-BY-NC-ND-4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/) | [SPDX](https://spdx.org/licenses/CC-BY-NC-ND-4.0.html) | *Use with caution* |

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
![](https://mirrors.creativecommons.org/presskit/icons/cc.svg) CC: Creative Commons licence

![](https://mirrors.creativecommons.org/presskit/icons/by.svg) BY: credit must be given to the creator.

![](https://mirrors.creativecommons.org/presskit/icons/sa.svg) SA: Adaptations must be shared under the same terms.

![](https://mirrors.creativecommons.org/presskit/icons/nc-eu.svg) NC: Only noncommercial uses of the work are permitted.

![](https://mirrors.creativecommons.org/presskit/icons/nd.svg) ND: No derivatives or adaptations of the work are permitted.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": ""} editable=true -->
### Selected German Licenses

| **License**      | **License URL** | **SPDX link** |
| --------------- | ----------------------------------- | ------------------------------------------ |
| dl-de/by-2-0    | [GovData](https://www.govdata.de/dl-de/by-2-0) | [SPDX](https://spdx.org/licenses/DL-DE-BY-2.0.html) |
| dl-de/zero-2-0  | [GovData](https://www.govdata.de/dl-de/zero-2-0) | [SPDX](https://spdx.org/licenses/DL-DE-ZERO-2.0.html) |


```{admonition} Note
:class: note
**dl-zero-de/2.0** is comparable to **CC0**

**dl-by-de/2.0** is comparable to **CC-BY-4.0** 
```


### Open Source Software Licenses

| **License**          | **License URL**                                    | **SPDX link** | **Comment**   |
|---------------------|--------------------------------------------------|--------------|--------------|
| GPL 3   | [GPL-3.0](https://www.gnu.org/licenses/gpl-3.0-standalone.html) | [SPDX](https://spdx.org/licenses/GPL-3.0-or-later.html) | Copyleft License\* |
| MIT   | [MIT License](https://opensource.org/license/mit) | [SPDX](https://spdx.org/licenses/MIT.html) | Permissive\*\*   |


\* **Copyleft:** Requires developers to license any modified versions under the same terms as the original version. It is a form of "share-alike" license.  
\*\* **Permissive:** Allows developers to use the original software in any project without licensing any changed versions under the original terms.


<!-- #endregion -->

<!-- #region slideshow={"slide_type": ""} editable=true -->
## References

```{bibliography}
:style: unsrt
:filter: docname in docnames
```
<!-- #endregion -->

```python slideshow={"slide_type": ""} editable=true

```
