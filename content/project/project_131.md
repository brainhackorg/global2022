{
  "Title": "Macapype: external pipeline",
  "link_to_issue": "https://github.com/brainhackorg/global2021/issues/131",
  "issue_number": 131,
  "labels": [
    {
      "name": "topic:tractography",
      "description": "",
      "color": "006b75"
    },
    {
      "name": "programming:workflows",
      "description": "nextflow",
      "color": "5319e7"
    },
    {
      "name": "tools:BIDS",
      "description": "",
      "color": "0052cc"
    },
    {
      "name": "status:web_ready",
      "description": "",
      "color": "0e8a16"
    },
    {
      "name": "programming:Python",
      "description": "",
      "color": "5319e7"
    },
    {
      "name": "topic:diffusion",
      "description": "",
      "color": "006b75"
    },
    {
      "name": "modality:MRI",
      "description": "",
      "color": "1d76db"
    },
    {
      "name": "bhg:marseille_fra_1",
      "description": "BHG 2021 Marseille event",
      "color": "d4c5f9"
    }
  ],
  "content": "<!-- Guidelines\r\n\r\nWe are very excited to meet you at the 2021 Brainhack Marseille \ud83c\udf89 To submit a project, you need to be an attendee of the 2021 Brainhack Marseille. We ask you to register first over here. Thank you!\r\n\r\nWe have prepared a checklist to help with your project submission. Here is how to proceed:\r\n\r\n1) Fill all the required project info part and upload a related image\r\n2) Check items in the checklist below as you go through them\r\n3) Once you are done, please delete the \"Guidelines\" section add a comment saying 'hi @Brainhack-Marseille/project-monitors: My project is ready!' You can check how your issue will appear by clicking on the 'preview' button under the issue title field. \r\nThank you!\r\n\r\nAfter this step (issue submition), we will assign a 'project monitor' to follow your submission. If at any time you need help or anything is unclear, please add a comment and ping your project monitor. Our team is here to help! -->\r\n\r\n## Project info\r\n\r\n**Title:**\r\nMacapype: external pipelines\r\n\r\n**Project lead and collaborators:**\r\nDavid Meunier \r\nKepkee Loh\r\nJulien Sein\r\nBastien Cagna\r\nOlivier Coulon\r\n\r\n**Description:**\r\nMacapype is a python package based on nipype, wrapping the tools required for NHP MRI anatomical segmentation. Macapype provide several processing pipelines, allowing optimisation and adaptation, depending on the quality of the images (SNR), acquisition sequences and antenna types, as well as species.\r\nToday, macapype is provided as a github repo, a pip install, and a docker/singularity image. The accepted inputs have to be in BIDS format, and macapype pipelines are callable thanks to a command line interface (CLI). \r\n\r\n**Links :**\r\nMacapype Github: https://github.com/Macatools/macapype\r\nMacapype Documentation: https://macatools.github.io/macapype/index.html\r\n\r\n**Goals for Brainhack Marseille**\r\nMacapype is mostly oriented to PNH anatomical segmentation. However, many applications can be included starting from a good segmentation quality : \r\n    \u2022 ACT (anatomically contrained tractography) from diffusion data, \r\n    \u2022 mesh and surfaces generation\r\nthat are not pure PNH but that are useful to be linked to macapype segementation. We would like to discuss the possibility of integration of this tools as external pipelines, i.e. not directly part of macapype, but that can be added in global workflows based on nipype.\r\n\r\n**Putative schedule :**\r\nMonday 6th of December , 2pm (Central Europe Time): presentation of macapype, past and future functionalities\r\nTuesday 7th of December, 2pm (CET) : diffusion and tractography of PNH data : discussion, and strategies\r\n\r\n\r\n\r\n**Required skills :**\r\nPNH anatomical MRI processing 30-100 %\r\npython 50-100 %\r\nnipype 30-100 %\r\n\r\n**Good first issues\u00a0:**\r\nWrapping in nipype a script to reorient anatomical image to normalized orientation\r\n\r\n**Striking Image**\r\n![macapype_logo_manon](https://user-images.githubusercontent.com/7290245/143407460-dee2115d-feb6-4089-b514-f2d19deef17b.jpg)\r\n"
}