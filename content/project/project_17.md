{
  "Title": "GPU implementation of Allen Brain V1 measured model using Julia and PyGeNN",
  "link_to_issue": "https://github.com/brainhackorg/global2022/issues/17",
  "issue_number": 17,
  "labels": [
    {
      "name": "sydney_aus",
      "description": "Sydney event",
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
      "name": "git_skills:1_commit_push",
      "description": "",
      "color": "bfdadc"
    },
    {
      "name": "programming:Julia",
      "description": "",
      "color": "5319e7"
    },
    {
      "name": "programming:documentation",
      "description": "Markdown, Sphinx",
      "color": "5319e7"
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
      "name": "project_type:documentation",
      "description": "",
      "color": "c5def5"
    },
    {
      "name": "topic:causality",
      "description": "",
      "color": "006b75"
    },
    {
      "name": "topic:data_visualisation",
      "description": "",
      "color": "006b75"
    },
    {
      "name": "project_development_status:0_concept_no_content",
      "description": "",
      "color": "bfd4f2"
    },
    {
      "name": "project_type:visualisation",
      "description": "",
      "color": "c5def5"
    },
    {
      "name": "status:web_ready",
      "description": "",
      "color": "0e8a16"
    },
    {
      "name": "topic:connectome",
      "description": "",
      "color": "006b75"
    },
    {
      "name": "project_type:method_development",
      "description": "",
      "color": "c5def5"
    },
    {
      "name": "topic:PCA",
      "description": "",
      "color": "006b75"
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
  "content": "### Title\r\n\r\nGPU implementation of Allen Brain V1 measured model using Julia and PyGeNN\r\n\r\n### Leaders  \r\n@russelljjarvis \r\n### Collaborators\r\n\r\n_No response_\r\n\r\n### Brainhack Global 2022 Event\r\n\r\nBrainhack Australasia\r\n\r\n### Project Description\r\n\r\n- It is often hard to access neuromorphic hardware as it is normally proprietary hardware and allocated based on competitive applications. Is applying for Neuromorphic hardware time efficient?\r\n- By contrast, many researchers have access too or can afford a GPU-enabled computer that can run Julia. Making Julia+GPU a more Democratic programming paradigm.\r\n- A lot of simulated biological network development time, is time spent debugging and developing models. Debugging execution runs, should be factored into the total execution time of a mode, ie the debugging and execution loop should be profiled too. In the past there may have been a tendency to overlook model construction delays that are caused by human errors.\r\n- From a green computing and environmental computing perspective, the total time from model conception to final model deploy is interesting.\r\n- How to get started?\r\n\r\n### Link to project repository/sources\r\n\r\nhttps://github.com/SpikingNetwork/TrainSpikingNet.jl\r\n\r\nA lot of the implied work is in wrangling the Pandas data-frame (drosophila) and Sonata HDF5 connectomes into Julia-compatible HDF5 and or compressed arrays saved as JLD2.\r\n\r\nThe code for getting Python connectomes is here:\r\n\r\nhttps://github.com/russelljjarvis/getConnectomes\r\n\r\n### Goals for Brain Hack Global\r\n\r\nApplying SNNs dynamic simulations to pre-existing connectome data.\r\n\r\nReproducing pre-existing computational research but using different more Democratic tools.\r\n\r\n### Good first issues\r\n\r\n1. issue one:\r\nWrangle drosophila, and vrat V1 Connectomes from [here ](https://github.com/russelljjarvis/getConnectomes\r\n)(Sonata/HDF5) to Julia JLD2 (also HDF5). This is not easy at all, and I am still working on this.\r\n\r\n2. issue two:\r\nMake dynamic time varying simulations by applying Ben Arthur's Spiking Neural Network code, to large scale spiking neural networks.\r\n\r\n* https://github.com/SpikingNetwork/TrainSpikingNet.jl\r\n\r\n* https://github.com/SpikingNetwork/distributedActivity\r\n\r\n3. Issue three Benchmark Ben Arthur's Julia code against PyGENN/CUDA, and ultimately Neuromorphic hardware applied to similar wired connectome.\r\n\r\n4. issue Four use PCA and UMAP on the output raster plot spike trains in Julia and or Python in order to understand and compare the output of the simulation.\r\n\r\n### Communication channels\r\n\r\nhttps://mattermost.brainhack.org/brainhack/channels/spikenetopt.jl\r\n\r\n### Skills\r\n\r\n- Julia\r\n- Python\r\n- GitHub\r\n- PCA, UMAP, dimensionality reduction\r\n\r\n### Onboarding documentation\r\n\r\nhttps://github.com/russelljjarvis/SpikeNetOpt.jl/blob/main/CONTRIBUTING.md\r\n\r\n### What will participants learn?\r\n\r\nJulia \r\n\r\n### Data to use\r\n\r\n* Janelia FlyEM drosophila connectome.\r\n* Allen Brain V1 connectome encoded in Sonata.\r\n\r\nhttps://github.com/russelljjarvis/getConnectomes\r\n\r\n### Number of collaborators\r\n\r\n>=1\r\n\r\n### Credit to collaborators\r\n\r\nI used all-contributors last year, and I think that will keep working well :)\r\n\r\nAlso co-authorship is a possibility? The goal is to publish something.\r\n\r\nhttps://github.com/russelljjarvis/SpikeNetOpt.jl/pull/17\r\n\r\n### Image\r\n\r\nLeave this text if you don't have an image yet. Pending\r\n\r\n### Type\r\n\r\ncoding_methods, method_development, visualization\r\n\r\n### Development status\r\n\r\n0_concept_no_content\r\n\r\n### Topic\r\n\r\ncausality, connectome, data_visualisation, physiology, reproducible_scientific_methods\r\n\r\n### Tools\r\n\r\nother\r\n\r\n### Programming language\r\n\r\nJulia\r\n\r\n### Modalities\r\n\r\nother\r\n\r\n### Git skills\r\n\r\n0_no_git_skills, 1_commit_push, 2_branches_PRs, 3_continuous_integration, 4_not_applicable\r\n\r\n### Anything else?\r\n\r\nThe other tool is really Julia code:\r\nhttps://github.com/SpikingNetwork/distributedActivity\r\nhttps://github.com/SpikingNetwork/TrainSpikingNet.jl\r\n\r\n### Things to do after the project is submitted and ready to review.\r\n\r\n- [X] Add a comment below the main post of your issue saying: `Hi @brainhackorg/project-monitors my project is ready!`\r\n- [X] Twitter-sized summary of your project pitch.",
  "project_url": "https://github.com/SpikingNetwork/TrainSpikingNet.jlA",
  "project_description": "\r\n\r\n- It is often hard to access neuromorphic hardware as it is normally proprietary hardware and allocated based on competitive applications. Is applying for Neuromorphic hardware time efficient?\r\n- By contrast, many researchers have access too or can afford a GPU-enabled computer that can run Julia. Making Julia+GPU a more Democratic programming paradigm.\r\n- A lot of simulated biological network development time, is time spent debugging and developing models. Debugging execution runs, should be factored into the total execution time of a mode, ie the debugging and execution loop should be profiled too. In the past there may have been a tendency to overlook model construction delays that are caused by human errors.\r\n- From a green computing and environmental computing perspective, the total time from model conception to final model deploy is interesting.\r\n- How to get started?\r\n\r\n"
}
