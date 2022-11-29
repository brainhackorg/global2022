{
  "Title": "Automatise your processing pipelines with nipype / pydra",
  "link_to_issue": "https://github.com/brainhackorg/global2022/issues/51",
  "issue_number": 51,
  "labels": [
    {
      "name": "marseille_fra",
      "description": "Marseille event",
      "color": "d4c5f9"
    },
    {
      "name": "git_skills:2_branches_PRs",
      "description": "",
      "color": "bfdadc"
    },
    {
      "name": "modality:MRI",
      "description": "",
      "color": "1d76db"
    },
    {
      "name": "modality:fMRI",
      "description": "",
      "color": "1d76db"
    },
    {
      "name": "programming:Matlab",
      "description": "",
      "color": "5319e7"
    },
    {
      "name": "modality:EEG",
      "description": "",
      "color": "1d76db"
    },
    {
      "name": "modality:MEG",
      "description": "",
      "color": "1d76db"
    },
    {
      "name": "tools:AFNI",
      "description": "",
      "color": "0052cc"
    },
    {
      "name": "programming:documentation",
      "description": "Markdown, Sphinx",
      "color": "5319e7"
    },
    {
      "name": "tools:Nipype",
      "description": "",
      "color": "0052cc"
    },
    {
      "name": "tools:BIDS",
      "description": "",
      "color": "0052cc"
    },
    {
      "name": "project",
      "description": "",
      "color": "f9bc70"
    },
    {
      "name": "tools:FSL",
      "description": "",
      "color": "0052cc"
    },
    {
      "name": "programming:Python",
      "description": "",
      "color": "5319e7"
    },
    {
      "name": "project_type:documentation",
      "description": "",
      "color": "c5def5"
    },
    {
      "name": "status:published",
      "description": "",
      "color": "0e8a16"
    },
    {
      "name": "tools:SPM",
      "description": "",
      "color": "0052cc"
    },
    {
      "name": "project_type:pipeline_development",
      "description": "",
      "color": "c5def5"
    },
    {
      "name": "project_development_status:0_concept_no_content",
      "description": "",
      "color": "bfd4f2"
    },
    {
      "name": "status:web_ready",
      "description": "",
      "color": "0e8a16"
    },
    {
      "name": "topic:reproducible_scientific_methods",
      "description": "",
      "color": "006b75"
    },
    {
      "name": "topic:physiology",
      "description": "",
      "color": "006b75"
    }
  ],
  "content": "### Title\r\n\r\nAutomatise your processing pipelines with nipype / pydra\r\n\r\n### Leaders\r\n\r\nDavid Meunier :\r\nTwitter: https://twitter.com/DavidM0579\r\nMattermost: @david.meunier https://mattermost.brainhack.org/brainhack\r\n\r\n\r\n### Collaborators\r\n\r\nTo fill at the end\r\n\r\n### Brainhack Global 2022 Event\r\n\r\nBrainhack Marseille\r\n\r\n### Project Description\r\n\r\nNeuroimaging and electrophysiology processing requires many steps, calling different softwares, possibly in different languages (typically, matlab batches or shell scripts).\r\n\r\nNipype has provided an integrative solution, with a sufficient level of complexity to cover most of the needs for writting pipelines in neuroimaging. It is based on the notion workflows, being an orderd succession of nodes, linking inputs and outputs. Nodes can be user-written function (in python), interfaces with existing softwares (e.g. FSL, AFNI or SPM), or even other user-defined sub-workflows.\r\n\r\nNipype is at the base of many widely used docker images, such as fmriprep and qsiprep. And has been extendend for other applications, such as EEG/MEG processing (ephypype), graph analysis in functional connectivity (graphpype) or non-human primate anatomical MRI segmentation (macapype).\r\n \r\nNipype has now achieved a degree of maturity to have become predominant in the community. But some of the limitations still prevails. It has decided in the last years to rewrite the core engine of nipype, to incorporate new functionnalities, such as runnnig containers as one node. The new implementation will be called pydra, and also still in its infancy, we expect it to become a major standard in the community.\r\n\r\n\r\n### Link to project repository/sources\r\n\r\n\r\nNipype:\r\nhttps://github.com/nipy/nipype\r\n\r\nPydra:\r\nhttps://github.com/nipype/pydra\r\n\r\nRelated projects:\r\nhttps://github.com/Macatools/macapype\r\n(potentially)\r\nhttps://github.com/neuropycon/ephypype\r\nhttps://github.com/neuropycon/graphpype\r\n\r\n### Goals for Brainhack Global\r\n\r\n\r\nIn this project, we propose :\r\n- to give an overview of how nipype works\r\n- to advise you if it is useful for your typical processing, \r\n- to help writting specific nodes or workflows dedicated to your processing.\r\n\r\nFor advaced users, We also propose:\r\n- to explain the advances of pydra compaired to nipype\r\n- to write some tools existing in nipype in pydra.\r\n\r\n\r\n\r\n### Good first issues\r\n\r\n- write an interface of your own python function  \r\n- build your own very simple processing pipelines with 2 nodes (possibly with your onw function) and one connection using pyBIDS inputs\r\n- convert an existing pipeline from nipype to pydra\r\n\r\n### Communication channels\r\n\r\nhttps://mattermost.brainhack.org/brainhack/channels/bhg22-marseille-auto-nipype-pydra\r\n\r\n### Skills\r\n\r\nNeuroimaging/electrophysiology processing: 100%\r\nShell Script / Matlab Batch: 75%\r\nPython: 50%\r\nNipype: 25%\r\n\r\n### Onboarding documentation\r\n\r\nhttps://macatools.github.io/macapype/contribute.html\r\n\r\n\r\n### What will participants learn?\r\n\r\nWriting easily modifiable and reusable pipeline; \r\nContributing to reproducible science\r\n\r\n### Data to use\r\n\r\nNone \r\n\r\n### Number of collaborators\r\n\r\n1\r\n\r\n### Credit to collaborators\r\n\r\nStarting a new pydra-based project will be rewarded as a main contributor to the project, and possibly as an author on a subsequent prospective (methological) article.\r\nWorking on your pipeline will be rewarded as your own github project.\r\n\r\n### Image\r\n\r\n\r\n![graph](https://user-images.githubusercontent.com/7290245/197730139-7d607b68-3cac-4241-8b2b-3145a7348254.png)\r\n\r\n\r\n### Type\r\n\r\npipeline_development\r\n\r\n### Development status\r\n\r\n0_concept_no_content\r\n\r\n### Topic\r\n\r\nreproducible_scientific_methods\r\n\r\n### Tools\r\n\r\nNipype\r\n\r\n### Programming language\r\n\r\nPython\r\n\r\n### Modalities\r\n\r\nfMRI\r\n\r\n### Git skills\r\n\r\n2_branches_PRs\r\n\r\n### Anything else?\r\n\r\nTesting is project template is directly usable on the website BrainHack Marseille 2022, \r\nSubject to modification.\r\n\r\n\r\n### Things to do after the project is submitted and ready to review.\r\n\r\n- [x] Add a comment below the main post of your issue saying: `Hi @brainhackorg/project-monitors my project is ready!`\r\n- [x] Twitter-sized summary of your project pitch.",
  "project_url": "Nipype:https://github.com/nipy/nipypePydra:https://github.com/nipype/pydraRelated",
  "project_description": "\r\n\r\nNeuroimaging and electrophysiology processing requires many steps, calling different softwares, possibly in different languages (typically, matlab batches or shell scripts).\r\n\r\nNipype has provided an integrative solution, with a sufficient level of complexity to cover most of the needs for writting pipelines in neuroimaging. It is based on the notion workflows, being an orderd succession of nodes, linking inputs and outputs. Nodes can be user-written function (in python), interfaces with existing softwares (e.g. FSL, AFNI or SPM), or even other user-defined sub-workflows.\r\n\r\nNipype is at the base of many widely used docker images, such as fmriprep and qsiprep. And has been extendend for other applications, such as EEG/MEG processing (ephypype), graph analysis in functional connectivity (graphpype) or non-human primate anatomical MRI segmentation (macapype).\r\n \r\nNipype has now achieved a degree of maturity to have become predominant in the community. But some of the limitations still prevails. It has decided in the last years to rewrite the core engine of nipype, to incorporate new functionnalities, such as runnnig containers as one node. The new implementation will be called pydra, and also still in its infancy, we expect it to become a major standard in the community.\r\n\r\n\r\n"
}
