{
  "Title": "Classification of Mild Cognitive Impairment(MCI) with machine learning models",
  "link_to_issue": "https://github.com/brainhackorg/global2021/issues/130",
  "issue_number": 130,
  "labels": [
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
      "name": "topic:machine_learning",
      "description": "",
      "color": "006b75"
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
      "name": "tools:SPM",
      "description": "",
      "color": "0052cc"
    },
    {
      "name": "topic:data_visualisation",
      "description": "",
      "color": "006b75"
    },
    {
      "name": "topic:deep_learning",
      "description": "",
      "color": "006b75"
    },
    {
      "name": "project",
      "description": "",
      "color": "f9bc70"
    },
    {
      "name": "topic:statistical_modelling",
      "description": "",
      "color": "006b75"
    },
    {
      "name": "project_development_status:2_releases_existing",
      "description": "",
      "color": "bfd4f2"
    },
    {
      "name": "project_type:coding_methods",
      "description": "",
      "color": "c5def5"
    },
    {
      "name": "status:web_ready",
      "description": "",
      "color": "0e8a16"
    },
    {
      "name": "tools:FSL",
      "description": "",
      "color": "0052cc"
    },
    {
      "name": "project_type:method_development",
      "description": "",
      "color": "c5def5"
    },
    {
      "name": "programming:R",
      "description": "",
      "color": "5319e7"
    },
    {
      "name": "programming:Python",
      "description": "",
      "color": "5319e7"
    },
    {
      "name": "tools:AFNI",
      "description": "",
      "color": "0052cc"
    },
    {
      "name": "project_type:documentation",
      "description": "",
      "color": "c5def5"
    },
    {
      "name": "modality:PET",
      "description": "",
      "color": "1d76db"
    },
    {
      "name": "modality:MRI",
      "description": "",
      "color": "1d76db"
    },
    {
      "name": "git_skills:2_branches_PRs",
      "description": "",
      "color": "bfdadc"
    },
    {
      "name": "project_type:visualisation",
      "description": "",
      "color": "c5def5"
    },
    {
      "name": "bhg:toronto_can_1",
      "description": "BHG 2021 Toronto event",
      "color": "d4c5f9"
    }
  ],
  "content": "### Title\r\n\r\nClassification of Mild Cognitive Impairment(MCI) with machine learning models \r\n\r\n### Leaders\r\n\r\nWei Shao\r\n\r\n### Collaborators\r\n\r\nTo be determined\r\n\r\n### Brainhack Global 2021 Event\r\n\r\nBrainHack Toronto\r\n\r\n### Project Description\r\n\r\n**- What are you doing, for whom, and why?**      \r\n \r\nRecent research has discovered that the subregions of hippocampus and medial temporal lobe (MTL) are related to Montreal Cognitive Assessment (MoCA) performance under a manual segmentation protocol. A significant volume reduction of anterolateral entorhinal cortex (alERC) has been found in the At-Risk group. This study also observed a positive linear relationship between MTL volumes and MoCA scores. Therefore, the aim of the project is to use machine learning models to analyze the structural data of MRIs. \r\n\r\nStarting from the regions of the hippocampus and medial temporal lobe, we will use automatic segmentation tools like FreeSurfer or ASHS to get the volume, thickness or curve of different brain regions from ADNI dataset as the input for different machine learning models to evaluate the model performance.\r\n\r\n**- What makes your project special and exciting?**\r\n\r\nAccording to previous studies, It is not easy to classify mild cognitive impairment from healthy people, given the fact that the change of brain structure is not very clear. The recent advance of statistical models, especially machine learning models, might provide an alternative solution for these issues.\r\n\r\n**- How to get started?**\r\n\r\nI have done some initial works. We can start from the introduction of data structure, models and the most interesting part, python!!! \r\n\r\n**- introduction with the data** \r\n\r\nThe Alzheimer\u2019s Disease Neuroimaging Initiative (ADNI) unites researchers with study data as they work to define the progression of Alzheimer\u2019s disease (AD). ADNI researchers collect, validate and utilize data, including MRI and PET images, genetics, cognitive tests, CSF and blood biomarkers as predictors of the disease. Study resources and data from the North American ADNI study are available through this website, including Alzheimer\u2019s disease patients, mild cognitive impairment subjects, and elderly controls.\r\n\r\n**- Where to find key resources?**\r\n\r\nhttps://neuroimage-book02.readthedocs.io/en/latest/\r\n\r\n### Link to project repository/sources\r\n\r\nhttps://github.com/WeiShaoD/MCI-Classification\r\n\r\n### Goals for Brainhack Global\r\n\r\n1. Gain the knowledge of structure of brain as well as how the brain change along with psychological disease\r\n2. Test the performance of different machine learning models for the brain structural data and find the best method to identify the MCI from healthy people.\r\n3. Deliever new insights to neuroscience community \r\n\r\n\r\n### Good first issues\r\n\r\n1. Process the MRIs scan\r\n2. Running with different models such as Rodam forest, multilayer perceptron and naive Bayes classifiers\r\n3. Interpret the result and gain the knowledge\r\n\r\n### Communication channels\r\n\r\nhttps://join.slack.com/t/mciclassifica-agm9145/shared_invite/zt-zbufngkk-F_XklCCFXTSi4vVIzy4CjQ\r\n\r\n### Skills\r\n\r\n- Coding: Python,  Shell-script \r\n- Non-Coding: statistical models. brain segmentation. psychological assessment. \r\n\r\n\r\n### Onboarding documentation\r\n\r\n_No response_\r\n\r\n### What will participants learn?\r\n\r\n1. Machine learning models \r\n2. Python\r\n3. Neuroimaging software and analysis methods (FreeSurfer, ASHS, FSL, AFNI or SPM)\r\n\r\n### Data to use\r\n\r\n**- introduction with the data** \r\n\r\nThe Alzheimer\u2019s Disease Neuroimaging Initiative (ADNI) unites researchers with study data as they work to define the progression of Alzheimer\u2019s disease (AD). ADNI researchers collect, validate and utilize data, including MRI and PET images, genetics, cognitive tests, CSF and blood biomarkers as predictors of the disease. Study resources and data from the North American ADNI study are available through this website, including Alzheimer\u2019s disease patients, mild cognitive impairment subjects, and elderly controls.\r\n\r\n### Number of collaborators\r\n\r\n1\r\n\r\n### Credit to collaborators\r\n\r\nsegmentation quality, psychological assessment, interpretation of results, preprocessing of data.\r\n\r\n### Image\r\n\r\nLeave this text if you don't have an image yet.\r\n\r\n### Type\r\n\r\ncoding_methods, method_development, visualization\r\n\r\n### Development status\r\n\r\n2_releases_existing\r\n\r\n### Topic\r\n\r\nbayesian_approaches, data_visualisation, deep_learning, machine_learning, MR_methodologies, statistical_modelling\r\n\r\n### Tools\r\n\r\nFreesurfer, Jupyter\r\n\r\n### Programming language\r\n\r\nPython, R\r\n\r\n### Modalities\r\n\r\nMRI\r\n\r\n### Git skills\r\n\r\n2_branches_PRs\r\n\r\n### Anything else?\r\n\r\n_No response_\r\n\r\n### Things to do after the project is submitted.\r\n\r\n- [X] Add a comment saying: `Hi @Brainhack-Global/project-monitors: my project is ready!`\r\n- [ ] Twitter-sized summary of your project pitch.",
  "project_url": "https://github.com/WeiShaoD/MCI-Classification",
  "project_description": "\r\n\r\n**- What are you doing, for whom, and why?**      \r\n \r\nRecent research has discovered that the subregions of hippocampus and medial temporal lobe (MTL) are related to Montreal Cognitive Assessment (MoCA) performance under a manual segmentation protocol. A significant volume reduction of anterolateral entorhinal cortex (alERC) has been found in the At-Risk group. This study also observed a positive linear relationship between MTL volumes and MoCA scores. Therefore, the aim of the project is to use machine learning models to analyze the structural data of MRIs. \r\n\r\nStarting from the regions of the hippocampus and medial temporal lobe, we will use automatic segmentation tools like FreeSurfer or ASHS to get the volume, thickness or curve of different brain regions from ADNI dataset as the input for different machine learning models to evaluate the model performance.\r\n\r\n**- What makes your project special and exciting?**\r\n\r\nAccording to previous studies, It is not easy to classify mild cognitive impairment from healthy people, given the fact that the change of brain structure is not very clear. The recent advance of statistical models, especially machine learning models, might provide an alternative solution for these issues.\r\n\r\n**- How to get started?**\r\n\r\nI have done some initial works. We can start from the introduction of data structure, models and the most interesting part, python!!! \r\n\r\n**- introduction with the data** \r\n\r\nThe Alzheimer\u2019s Disease Neuroimaging Initiative (ADNI) unites researchers with study data as they work to define the progression of Alzheimer\u2019s disease (AD). ADNI researchers collect, validate and utilize data, including MRI and PET images, genetics, cognitive tests, CSF and blood biomarkers as predictors of the disease. Study resources and data from the North American ADNI study are available through this website, including Alzheimer\u2019s disease patients, mild cognitive impairment subjects, and elderly controls.\r\n\r\n**- Where to find key resources?**\r\n\r\nhttps://neuroimage-book02.readthedocs.io/en/latest/\r\n\r\n"
}