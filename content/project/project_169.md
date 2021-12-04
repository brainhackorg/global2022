{
  "Title": "Tools for MRI diffusion in human and non-human primates",
  "link_to_issue": "https://github.com/brainhackorg/global2021/issues/169",
  "issue_number": 169,
  "labels": [
    {
      "name": "git_skills:0_none",
      "description": "",
      "color": "bfdadc"
    },
    {
      "name": "programming:containerization",
      "description": "Docker, Singularity",
      "color": "5319e7"
    },
    {
      "name": "programming:documentation",
      "description": "Markdown, Sphinx",
      "color": "5319e7"
    },
    {
      "name": "topic:MR_methodologies",
      "description": "",
      "color": "006b75"
    },
    {
      "name": "programming:shell_scripting",
      "description": "",
      "color": "5319e7"
    },
    {
      "name": "project_type:pipeline_development",
      "description": "",
      "color": "c5def5"
    },
    {
      "name": "tools:Freesurfer",
      "description": "",
      "color": "0052cc"
    },
    {
      "name": "tools:Jupyter",
      "description": "",
      "color": "0052cc"
    },
    {
      "name": "topic:tractography",
      "description": "",
      "color": "006b75"
    },
    {
      "name": "topic:data_visualisation",
      "description": "",
      "color": "006b75"
    },
    {
      "name": "project_tools_skills:expert",
      "description": "",
      "color": "c2e0c6"
    },
    {
      "name": "project",
      "description": "",
      "color": "f9bc70"
    },
    {
      "name": "project_type:coding_methods",
      "description": "",
      "color": "c5def5"
    },
    {
      "name": "tools:DIPY",
      "description": "",
      "color": "0052cc"
    },
    {
      "name": "status:web_ready",
      "description": "",
      "color": "0e8a16"
    },
    {
      "name": "tools:MRtrix",
      "description": "",
      "color": "0052cc"
    },
    {
      "name": "tools:FSL",
      "description": "",
      "color": "0052cc"
    },
    {
      "name": "modality:DWI",
      "description": "",
      "color": "1d76db"
    },
    {
      "name": "topic:reproducible_scientific_methods",
      "description": "",
      "color": "006b75"
    },
    {
      "name": "project_development_status:0_concept_no_content",
      "description": "",
      "color": "bfd4f2"
    },
    {
      "name": "programming:Python",
      "description": "",
      "color": "5319e7"
    },
    {
      "name": "programming:Unix_command_line",
      "description": "",
      "color": "5319e7"
    },
    {
      "name": "git_skills:1_commit_push",
      "description": "",
      "color": "bfdadc"
    },
    {
      "name": "project_type:documentation",
      "description": "",
      "color": "c5def5"
    },
    {
      "name": "topic:connectome",
      "description": "",
      "color": "006b75"
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
      "name": "project_type:visualisation",
      "description": "",
      "color": "c5def5"
    },
    {
      "name": "bhg:marseille_fra_1",
      "description": "BHG 2021 Marseille event",
      "color": "d4c5f9"
    }
  ],
  "content": "### Title\r\n\r\nTools for MRI diffusion in human and non-human primates\r\n\r\n### Leaders\r\n\r\n- Julien Sein (@julfou81)\r\n- David Meunier\r\n- Arnaud Le Troter\r\n- Hugo Dary\r\n\r\n### Collaborators\r\n\r\n_No response_\r\n\r\n### Brainhack Global 2021 Event\r\n\r\nBrainhack Marseille\r\n\r\n### Project Description\r\n\r\nThere are many pipelines for processing diffusion MRI data (diffuse, qsiprep, mrtrix pipelines, FSL pipelines, dipy, Designer, etc.). For newcomers in the field of Diffusion MRI, it may be overwhelming to pick the tools that best fits the needs, as well as to define the needs themselves.\r\n\r\n*(NHP specific)* : NHP image processing has specific challenges such as image reorientation, which can be more tricky when the Diffusion Vectors as to follow the transformation applied to the diffusion images.\r\n\r\nWe aim at sharing expertise, identify specific problems encountered by users, and define quality metrics (quality of orientation vectors, qualitative and quantitative quality check of processing stages) \r\n\r\n*(NHP specific)*\u00a0: We also aim at integrating segmentations computed externally to mrtrix and FSL pipelines, that are non-specific pipelines (i.e. also available for human images) \r\n\r\n**Skills:**\r\n\r\n- MRI diffusion (general knowledge) 50%\r\n- MRI processing 50%\r\n- pipelining (30-70%)\r\n\r\n**Communication channels\u00a0:**\r\n\r\n- https://mattermost.brainhack.org/brainhack/channels/mri_diffusion\r\n- https://github.com/Centre-IRM-INT/MRI_Diffusion\r\n- https://univ-amu-fr.zoom.us/j/92141093977?pwd=cEorbHI3bzVFZlVwSE9FRVZiaUNGZz09\r\n\r\n\r\n**Programed schedule**\r\n\r\nTuesday 7th December, 2pm CET\u00a0: discussion on tools and pipelines for MRI diffusion processing\r\n\r\n\r\n### Link to project repository/sources\r\n\r\nhttps://github.com/Centre-IRM-INT/MRI_Diffusion\r\n\r\n### Good first issues\r\n\r\n1. Share your experience with Diffusion MRI \r\n2. Share the difficulties you encountered with Diffusion MRI processing \r\n\r\n### Skills\r\n\r\n- MRI diffusion (general knowledge) 50%\r\n- MRI processing 50%\r\n- pipelining (30-70%)\r\n\r\n### Onboarding documentation\r\n\r\n_No response_\r\n\r\n### What will participants learn?\r\n\r\nParticipant will learn about all the wonderful tools are already present out there and hopefully they will find the ones that best fit their needs.\r\nThey may also find new solutions to process diffusion in NHP (non-human primate) images.\r\n\r\n### Data to use\r\n\r\n_No response_\r\n\r\n### Number of collaborators\r\n\r\nmore\r\n\r\n### Credit to collaborators\r\n\r\nProject contributor are listed on the README file of the project GitHub page\r\n\r\n### Image\r\n\r\n![Noe_tracto](https://user-images.githubusercontent.com/32452352/144453670-feebbfb9-1f64-43e2-9f6f-cdb4ba051f7e.png)\r\n\r\n\r\n### Type\r\n\r\ncoding_methods, documentation, pipeline_development\r\n\r\n### Development status\r\n\r\n0_concept_no_content\r\n\r\n### Topic\r\n\r\nconnectome, data_visualisation, diffusion, MR_methodologies, reproducible_scientific_methods, tractography\r\n\r\n### Tools\r\n\r\nDIPY, Freesurfer, FSL, Jupyter, MRtrix, Nipype\r\n\r\n### Programming language\r\n\r\ncontainerization, documentation, Python, shell_scripting, unix_command_line\r\n\r\n### Modalities\r\n\r\nDWI, MRI\r\n\r\n### Git skills\r\n\r\n0_no_git_skills, 1_commit_push\r\n\r\n### Anything else?\r\n\r\n_No response_\r\n\r\n### Things to do after the project is submitted and ready to review.\r\n\r\n- [X] Add a comment below the main post of your issue saying: `Hi @brainhackorg/project-monitors my project is ready!`\r\n- [X] Twitter-sized summary of your project pitch.",
  "project_url": "https://github.com/Centre-IRM-INT/MRI_Diffusion",
  "project_description": "\r\n\r\nThere are many pipelines for processing diffusion MRI data (diffuse, qsiprep, mrtrix pipelines, FSL pipelines, dipy, Designer, etc.). For newcomers in the field of Diffusion MRI, it may be overwhelming to pick the tools that best fits the needs, as well as to define the needs themselves.\r\n\r\n*(NHP specific)* : NHP image processing has specific challenges such as image reorientation, which can be more tricky when the Diffusion Vectors as to follow the transformation applied to the diffusion images.\r\n\r\nWe aim at sharing expertise, identify specific problems encountered by users, and define quality metrics (quality of orientation vectors, qualitative and quantitative quality check of processing stages) \r\n\r\n*(NHP specific)*\u00a0: We also aim at integrating segmentations computed externally to mrtrix and FSL pipelines, that are non-specific pipelines (i.e. also available for human images) \r\n\r\n**Skills:**\r\n\r\n- MRI diffusion (general knowledge) 50%\r\n- MRI processing 50%\r\n- pipelining (30-70%)\r\n\r\n**Communication channels\u00a0:**\r\n\r\n- https://mattermost.brainhack.org/brainhack/channels/mri_diffusion\r\n- https://github.com/Centre-IRM-INT/MRI_Diffusion\r\n- https://univ-amu-fr.zoom.us/j/92141093977?pwd=cEorbHI3bzVFZlVwSE9FRVZiaUNGZz09\r\n\r\n\r\n**Programed schedule**\r\n\r\nTuesday 7th December, 2pm CET\u00a0: discussion on tools and pipelines for MRI diffusion processing\r\n\r\n\r\n"
}