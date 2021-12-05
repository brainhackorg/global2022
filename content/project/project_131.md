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
      "name": "tools:Nipype",
      "description": "",
      "color": "0052cc"
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
  "content": "## Project info\r\n\r\n**Title:**\r\nMacapype: external pipelines\r\n\r\n**Project lead and collaborators:**\r\n\r\n- David Meunier \r\n- Kepkee Loh\r\n- Julien Sein\r\n- Bastien Cagna\r\n- Olivier Coulon\r\n\r\n**Description:**\r\nMacapype is a python package based on nipype, wrapping the tools required for NHP MRI anatomical segmentation. Macapype provide several processing pipelines, allowing optimisation and adaptation, depending on the quality of the images (SNR), acquisition sequences and antenna types, as well as species.\r\nToday, macapype is provided as a github repo, a pip install, and a docker/singularity image. The accepted inputs have to be in BIDS format, and macapype pipelines are callable thanks to a command line interface (CLI). \r\n\r\n**Links :**\r\nMacapype Github: https://github.com/Macatools/macapype\r\nMacapype Documentation: https://macatools.github.io/macapype/index.html\r\n\r\n**Goals for Brainhack Marseille**\r\nMacapype is mostly oriented to PNH anatomical segmentation. However, many applications can be included starting from a good segmentation quality : \r\n- ACT (anatomically contrained tractography) from diffusion data, \r\n- mesh and surfaces generation\r\nthat are not pure PNH but that are useful to be linked to macapype segementation. We would like to discuss the possibility of integration of this tools as external pipelines, i.e. not directly part of macapype, but that can be added in global workflows based on nipype.\r\n\r\n**Putative schedule :**\r\n- Monday 6th of December , 2pm (Central Europe Time): presentation of macapype, past and future functionalities\r\n- Tuesday 7th of December, 2pm (CET) : diffusion and tractography of PNH data : discussion, and strategies\r\n\r\n**Communication channels:**\r\n- mattermost: https://mattermost.brainhack.org/brainhack/channels/primedre-brainhack-2021-macapype\r\n- zoom channel: https://univ-amu-fr.zoom.us/j/94628657623?pwd=bG5ZdnArcEtLanVNcktFSjdaMG5OUT09\r\n\r\n**Required skills :**\r\n- PNH anatomical MRI processing 30-100 %\r\n- Python 50-100 %\r\n- Nipype 30-100 %\r\n\r\n**Good first issues\u00a0:**\r\nWrapping in nipype a script to reorient anatomical image to normalized orientation\r\n\r\n**Striking Image**\r\n![macapype_logo_manon](https://user-images.githubusercontent.com/7290245/143407460-dee2115d-feb6-4089-b514-f2d19deef17b.jpg)\r\n"
}