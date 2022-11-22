{
  "Title": "Bayes on the Brain in Python",
  "link_to_issue": "https://github.com/brainhackorg/global2022/issues/78",
  "issue_number": 78,
  "labels": [
    {
      "name": "australasia_aus",
      "description": "Australasia event",
      "color": "d4c5f9"
    },
    {
      "name": "git_skills:0_none",
      "description": "",
      "color": "bfdadc"
    },
    {
      "name": "git_skills:3_continuous_integration",
      "description": "",
      "color": "bfdadc"
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
      "name": "git_skills:1_commit_push",
      "description": "",
      "color": "bfdadc"
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
      "name": "programming:Python",
      "description": "",
      "color": "5319e7"
    },
    {
      "name": "project_type:coding_methods",
      "description": "",
      "color": "c5def5"
    },
    {
      "name": "project_development_status:1_basic structure",
      "description": "",
      "color": "bfd4f2"
    },
    {
      "name": "project_type:documentation",
      "description": "",
      "color": "c5def5"
    },
    {
      "name": "tools:fMRIPrep",
      "description": "",
      "color": "0052cc"
    },
    {
      "name": "tools:Jupyter",
      "description": "",
      "color": "0052cc"
    },
    {
      "name": "status:published",
      "description": "",
      "color": "0e8a16"
    },
    {
      "name": "programming:R",
      "description": "",
      "color": "5319e7"
    },
    {
      "name": "project_type:pipeline_development",
      "description": "",
      "color": "c5def5"
    },
    {
      "name": "status:web_ready",
      "description": "",
      "color": "0e8a16"
    },
    {
      "name": "project_type:method_development",
      "description": "",
      "color": "c5def5"
    },
    {
      "name": "topic:MR_methodologies",
      "description": "",
      "color": "006b75"
    },
    {
      "name": "topic:reproducible_scientific_methods",
      "description": "",
      "color": "006b75"
    },
    {
      "name": "topic:statistical_modelling",
      "description": "",
      "color": "006b75"
    }
  ],
  "content": "### Title\r\n\r\nBayes on the Brain in Python\r\n\r\n### Leaders\r\n\r\nKelly Garner\r\nmastodon: [garner_theory@fediscience.org](https://fediscience.org/web/@garner_theory)\r\ngithub: [kel-github](https://github.com/kel-github) \r\nmattermost: @kels\r\n\r\nGang Chen\r\ntwitter: [@gangchen6](https://twitter.com/gangchen6?lang=en)\r\ngithub: [afni-gangc](https://github.com/afni-gangc) \r\nmattermost: @gangchen\r\n\r\n### Collaborators\r\n\r\nChristopher Nolan \r\nmastodon: [@cnolan@fediscience.org](https://fediscience.org/web/@cnolan)\r\ngithub: [crnolan](https://github.com/crnolan)\r\n\r\n### Brainhack Global 2022 Event\r\n\r\nBrainhack Australasia\r\n\r\n### Project Description\r\n\r\nHuman brain imaging data is massively multidimensional, yet current approaches to modeling functional brain responses apply univariate tests to each voxel separately. This leads to controlling for a vast number of statistical inferences, and to an implicit but unrealistic assumption of a uniform distribution over voxels \u2013 no information is shared across the brain.  \r\n\r\nA more reasoned approach to assessing regional activity focuses on estimating the strength of an effect; this can be achieved readily under a Bayesian multilevel modeling framework. A further advantage to this approach is that you can build in better assumptions about the data (e.g. normality across space, see [Chen et al, 2019, Neuroinformatics](https://doi.org/10.1007/s12021-018-9409-6) and eradicate the need for adjusting for masses of simultaneous statistical inferences.  \r\n\r\nApplying such a Bayesian multilevel modeling framework to the analysis of fMRI data is in its infancy. The methodology has been implemented at the region level into the AFNI programme (see [Chen et al, 2022, Aperture Neuro](http://dx.doi.org/10.52294/2e179dbf-5e37-4338-a639-9ceb92b055ea), using Stan through the R package BRMS (Burkner et al, 2017, Journal of Statistical Software). At OHBM Brainhack 2022, we also implemented this methodology in Python using the PyMC framework (Salvatier et al, 2016, PeerJ Computer Science) and the Bambi interface (Capretto et al, 2022, Journal of Statistical Software).  \r\n\r\nAt Brainhack Global 2022, we will be expanding the capability of the Python implementation. We will:  \r\n\r\n- Test the computational limits of the approach - can we model activity at the voxel (as opposed to regional) level? What are the run times for voxel-based models, for many subjects or more complex models?  \r\n- Build a workflow and a tutorial document to equip anyone to use the method.   \r\n\r\nOur long term goal is to build a python interface and this is the first step!   \r\n\r\nTo get started, take a look at Chen (2022, see above) for more details on the method. Also [check out our implementation in Python](https://github.com/crnolan/pyrba)\r\n\r\n### Link to project repository/sources\r\n\r\nRepo:  \r\nhttps://github.com/crnolan/pyrba  \r\n\r\nResources  \r\nhttps://bambinos.github.io/bambi/main/index.html  \r\nhttps://www.pymc.io/projects/docs/en/stable/learn.html  \r\nhttps://nilab-uva.github.io/AOMIC.github.io/  \r\n{Chen et al, 2022, Aperture Neuro](http://dx.doi.org/10.52294/2e179dbf-5e37-4338-a639-9ceb92b055ea)  \r\n\r\n### Goals for Brainhack Global\r\n\r\n- Test for computational limitations of applying a Bayesian multilevel framework to fMRI data analysis  \r\n\r\n- Build a jupyter notebook tutorial workflow that includes model definition, fitting, quality checks, and results interpretation  \r\n\r\n-  Start translating the notebook into a Python interface for the people!\r\n\r\n\r\n### Good first issues\r\n\r\n1. Have a go at using the current Python implementation in a Jupyter notebook  \r\n2. Add a sample of the open dataset to the cloud server.   \r\n3. Run through the PyMC, Bambi and brms tutorials to find any key differences (e.g. with regard to priors etc)  \r\n4. Define a model to be run at the voxel level. Calculate compute time.  \r\n\r\n\r\n\r\n### Communication channels\r\n\r\nmattermost channel: [bayes-on-the-brain](https://mattermost.brainhack.org/brainhack/channels/bayes-on-the-brain)  \r\n\r\n\r\n### Skills\r\n\r\n- Python \r\n- Bayesian modeling analysis  \r\n- fMRI data analysis  \r\n- Github  \r\n- R  \r\n- Interest and enthusiasm :)\r\n\r\n\r\n### Onboarding documentation\r\n\r\nSee the link to the project repository and resources.\r\n\r\n### What will participants learn?\r\n\r\n- Python \r\n- Bayesian multilevel modeling \r\n- fMRI data analysis\r\n- Github\r\n- R\r\n\r\n\r\n### Data to use\r\n\r\nhttps://nilab-uva.github.io/AOMIC.github.io/\r\n\r\n### Number of collaborators\r\n\r\nmore\r\n\r\n### Credit to collaborators\r\n\r\nProject contributors will be listed on the project README and included as authors on any further outputs.\r\n\r\n### Image\r\n\r\nLeave this text if you don't have an image yet.\r\n![project-image](https://user-images.githubusercontent.com/7220723/201803083-16858c76-bec4-45bd-8bb6-86baff84fcac.png)\r\n\r\n\r\n### Type\r\n\r\ncoding_methods, method_development, pipeline_development\r\n\r\n### Development status\r\n\r\n1_basic structure\r\n\r\n### Topic\r\n\r\nbayesian_approaches, MR_methodologies, reproducible_scientific_methods, statistical_modelling\r\n\r\n### Tools\r\n\r\nAFNI, BIDS, fMRIPrep, Jupyter, other\r\n\r\n### Programming language\r\n\r\ndocumentation, Python, `R`\r\n\r\n### Modalities\r\n\r\nfMRI\r\n\r\n### Git skills\r\n\r\n0_no_git_skills, 1_commit_push, 2_branches_PRs, 3_continuous_integration\r\n\r\n### Anything else?\r\n\r\n_No response_\r\n\r\n### Things to do after the project is submitted and ready to review.\r\n\r\n- [X] Add a comment below the main post of your issue saying: `Hi @brainhackorg/project-monitors my project is ready!`\r\n- [X] Twitter-sized summary of your project pitch.",
  "project_url": "https://github.com/crnolan/pyrba",
  "project_description": "\r\n\r\nHuman brain imaging data is massively multidimensional, yet current approaches to modeling functional brain responses apply univariate tests to each voxel separately. This leads to controlling for a vast number of statistical inferences, and to an implicit but unrealistic assumption of a uniform distribution over voxels \u2013 no information is shared across the brain.  \r\n\r\nA more reasoned approach to assessing regional activity focuses on estimating the strength of an effect; this can be achieved readily under a Bayesian multilevel modeling framework. A further advantage to this approach is that you can build in better assumptions about the data (e.g. normality across space, see [Chen et al, 2019, Neuroinformatics](https://doi.org/10.1007/s12021-018-9409-6) and eradicate the need for adjusting for masses of simultaneous statistical inferences.  \r\n\r\nApplying such a Bayesian multilevel modeling framework to the analysis of fMRI data is in its infancy. The methodology has been implemented at the region level into the AFNI programme (see [Chen et al, 2022, Aperture Neuro](http://dx.doi.org/10.52294/2e179dbf-5e37-4338-a639-9ceb92b055ea), using Stan through the R package BRMS (Burkner et al, 2017, Journal of Statistical Software). At OHBM Brainhack 2022, we also implemented this methodology in Python using the PyMC framework (Salvatier et al, 2016, PeerJ Computer Science) and the Bambi interface (Capretto et al, 2022, Journal of Statistical Software).  \r\n\r\nAt Brainhack Global 2022, we will be expanding the capability of the Python implementation. We will:  \r\n\r\n- Test the computational limits of the approach - can we model activity at the voxel (as opposed to regional) level? What are the run times for voxel-based models, for many subjects or more complex models?  \r\n- Build a workflow and a tutorial document to equip anyone to use the method.   \r\n\r\nOur long term goal is to build a python interface and this is the first step!   \r\n\r\nTo get started, take a look at Chen (2022, see above) for more details on the method. Also [check out our implementation in Python](https://github.com/crnolan/pyrba)\r\n\r\n"
}
