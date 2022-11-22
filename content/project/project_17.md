{
  "Title": "Large Scale FPGA Neuromorphic Interface precursor work. A GPU implementation of Allen Brain V1 measured model using Julia and or PyGeNN",
  "link_to_issue": "https://github.com/brainhackorg/global2022/issues/17",
  "issue_number": 17,
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
      "name": "status:published",
      "description": "",
      "color": "0e8a16"
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
  "content": "### Title\r\n\r\nGPU implementation of Allen Brain V1 measured model using Julia and or PyGeNN: A precursor to a large scale FPGA based very large scale spiking neuronal network.\r\n\r\n### Leaders  \r\n@russelljjarvis \r\n### Collaborators\r\n\r\n_No response_\r\n\r\n### Brainhack Global 2022 Event\r\n\r\nBrainhack Australasia\r\n\r\n### Project Description\r\n\r\n\r\n- Providing a ground truth for an FPGA based large scale simulation.\r\n- Making Julia+GPU potentially a more Democratic programming paradigm.\r\n- A lot of simulated biological network development time is time spent debugging and developing models. \r\n- For large-scale spike trains the performance of plotting code becomes an important issue too, given that plotting may happen many times during model development.\r\n- Debugging execution runs should be factored into the total execution time of a mode, ie the debugging and execution loop should be profiled too. In the past, there may have been a tendency to overlook model construction delays that are caused by human errors.\r\n- From a green computing and environmental computing perspective, the total time from model conception to final model deployment is interesting.\r\n\r\n### How to get started?\r\n\r\ncode entry point is ```bash workflow.sh```\r\nBut it assumes you first followed the install intructions in the [README.md here](https://github.com/SpikingNetwork/TrainSpikingNet.jl\r\n)\r\nhttps://github.com/JuliaWSU/TrainSpikingNet.jl/blob/master/workflow.sh\r\n\r\n#### Link to project repository/sources\r\n\r\nThrough pers-comm I have established that the author of the original repository may be open to PRs.\r\n\r\nhttps://github.com/SpikingNetwork/TrainSpikingNet.jl\r\n\r\nHowever there exist some more experimental forks for intermediate hacking. Another fork of TrainSpikingNet is [here](https://github.com/JuliaWSU/TrainSpikingNet.jl)\r\n\r\nA lot of the implied work is in wrangling the Pandas data frame and Sonata HDF5 connectomes into Julia-compatible HDF5 and or compressed arrays saved as JLD2.\r\n\r\nThe code for getting Python connectomes is [here]\r\n(https://github.com/williamsnider/v1_project/blob/main/build_model.py)\r\n\r\n### Goals for Brain Hack Global\r\n\r\nApplying SNNs dynamic simulations to pre-existing connectome data.\r\n\r\nReproducing pre-existing computational research but using different more Democratic tools.\r\n\r\n### Good First Issues:\r\n# 1.\r\nUse PCA and UMAP on the output raster plot spike trains in Julia and or Python in order to understand and compare the output of the simulation [Done, or done for a trivially small spike time raster plot].\r\n\r\nPossibly the easiest immediate thing someone could get working:\r\nApply sequence detection to the spike trains too via PPSeq.jl\r\nhttps://github.com/lindermanlab/PPSeq.jl\r\nhttps://github.com/JuliaWSU/TrainSpikingNet.jl/blob/master/src/plot.jl#L72\r\nApply PPSeq.jl to the spike train array: nss\r\n\r\n# 2.\r\nUse Do community partitioning on the static adjacency (connection) matrix, using any approach that works (maybe even do this using Pythons networkx). Networkx community partitioning algorithms like Louvain would expect your network to be un-directed. Networkx has a constructor for making an undirected network, from a numpy matrix input.\r\nIssues here are making the network connection matrix (Hermitian) and or Symmetric. Julia has two packages (https://github.com/bicycle1885/Leiden.jl, and METIS). Metis expects a matrix of Integers rather than float Real numbers between [0,1] as is common for synaptic weights.\r\n\r\nNote these people have made progress on graph analysis of biological neural networks:\r\nrealneuralnetworks\r\nhttps://github.com/jingpengw/realneuralnetworks-notebook/blob/main/34_connectivity_analysis/ju_connectivity_graph.ipynb\r\n\r\nNote these people (realneuralnetworks) have made progress on graph analysis of biological neural networks, it is unknown if their approach scales well. If it does give credit and re-purpose their methods.\r\nhttps://github.com/jingpengw/realneuralnetworks-notebook/blob/main/34_connectivity_analysis/ju_connectivity_graph.ipynb\r\nhttps://github.com/jingpengw/realneuralnetworks-notebook/blob/main/34_connectivity_analysis/ju_connection-psd.ipynb\r\n\r\nJulia Light Graphs also supports community partitioning. Issues I have experienced for light graphs partitioning are (1 running out of memory). and 2. Matrix is not symmetric and or Hermitian.\r\n\r\nHPC (Gadi) may solve the memory issue.\r\n[Julia Graph partitioning](https://docs.juliahub.com/LightGraphs/Xm08G/1.3.5/community/#LightGraphs.label_propagation-Union%7BTuple%7BAbstractGraph%7BT%7D%7D,%20Tuple%7BT%7D,%20Tuple%7BAbstractGraph%7BT%7D,Any%7D%7D%20where%20T)\r\n\r\n## Good Advanced Issues\r\n# 1.\r\nRat V1 Connectomes fromWrangle Rat V1 Connectomes from Sonata HDF5/Python to Julia [here ](https://github.com/russelljjarvis/getConnectomes)(Sonata/HDF5) to Julia JLD2 (also HDF5).\r\n\r\nThis is partially done. See for example here:\r\nhttps://github.com/russelljjarvis/TrainSpikingNet.jl/blob/master/src/fast_connection_matrices.jl#L1_L67\r\n\r\nHowever, it would be good to compare this against the PyGeNN connectome (which uses different indexing). Also, I have only done this for a partition of this enormous connectome. See discussion here: https://github.com/russelljjarvis/TrainSpikingNet.jl/discussions/5#discussioncomment-4112622\r\n\r\n# 2.\r\nMake dynamic time-varying simulations by applying Ben Arthur's Spiking Neural Network code, to large-scale spiking neural networks.\r\n\r\nhttps://github.com/SpikingNetwork/TrainSpikingNet.jl\r\nOne big issue here is that connection matrix-building methods are read in from a sequence of files that defines all the parameters of a simulation. Finally, a plethora of different connection matrix variables is embedded in a Julia static struct. The dimensionality of these matrices needs to be compatible with input stimulus dimensions. Compared to Python, plugging in new connection matrices is delicate and some care and understanding of Julia structs is required. See discussion here: https://github.com/russelljjarvis/TrainSpikingNet.jl/discussions/5#discussioncomment-4112622\r\n\r\nCan we simply use https://github.com/rafaqz/Mixers.jl to make a copy of the original struct and add in replacement matrices to a the cloned struct instance?\r\n\r\nAnother issue is wrangling the Sonata defined artificial synaptic inputs to make them compatible with TrainSpikingNet.jl\r\n\r\n# 3.\r\nSilence the correlation-based spike time training parts of the simulation workflow, as we are not yet training a network, but instead are just simulating it. Decoupling this code may be tricky.\r\n\r\n# 4.\r\nBenchmark Ben Arthur's Julia code against PyGENN/CUDA, and ultimately Neuromorphic hardware applied to similarly wired connectome.\r\n\r\nhttps://github.com/russelljjarvis/v1_project\r\n\r\n\r\n### Communication channels\r\n\r\nhttps://mattermost.brainhack.org/brainhack/channels/spikenetopt.jl\r\n\r\n### Skills\r\n\r\n- Julia\r\n- Python\r\n- GitHub\r\n\r\n### Onboarding documentation\r\n\r\nhttps://github.com/russelljjarvis/SpikeNetOpt.jl/blob/main/CONTRIBUTING.md\r\n\r\n### What will participants learn?\r\n\r\nJulia \r\n\r\n### Data to use\r\n\r\n* Allen Brain V1 connectome encoded in Sonata.\r\n\r\nhttps://github.com/russelljjarvis/getConnectomes\r\n\r\n### Number of collaborators\r\n\r\n`>=1`\r\n\r\n### Credit to collaborators\r\n\r\nI used all-contributors last year, and I think that will keep working well :)\r\n\r\nAlso co-authorship is a possibility? The goal is to publish something.\r\n\r\nhttps://github.com/russelljjarvis/SpikeNetOpt.jl/pull/17\r\n\r\n### Image\r\n\r\nLeave this text if you don't have an image yet. Pending\r\n\r\n### Type\r\n\r\ncoding_methods, method_development, visualization\r\n\r\n### Development status\r\n\r\n0_concept_no_content\r\n\r\n### Topic\r\n\r\nconnectome, data_visualisation, physiology, reproducible_scientific_methods\r\n\r\n### Tools\r\n\r\nother\r\n\r\n### Programming language\r\n\r\nJulia, Python, CUDA.\r\n\r\n### Modalities\r\n\r\nother\r\n\r\n### Git skills\r\n\r\n0_no_git_skills, 1_commit_push, 2_branches_PRs, 3_continuous_integration, 4_not_applicable\r\n\r\n### Things to do after the project is submitted and ready to review.\r\n\r\n- [X] Add a comment below the main post of your issue saying: `Hi @brainhackorg/project-monitors my project is ready!`\r\n- [X] Twitter-sized summary of your project pitch.",
  "project_url": "PRs.https://github.com/SpikingNetwork/TrainSpikingNet.jlHowever",
  "project_description": "\r\n\r\n\r\n- Providing a ground truth for an FPGA based large scale simulation.\r\n- Making Julia+GPU potentially a more Democratic programming paradigm.\r\n- A lot of simulated biological network development time is time spent debugging and developing models. \r\n- For large-scale spike trains the performance of plotting code becomes an important issue too, given that plotting may happen many times during model development.\r\n- Debugging execution runs should be factored into the total execution time of a mode, ie the debugging and execution loop should be profiled too. In the past, there may have been a tendency to overlook model construction delays that are caused by human errors.\r\n- From a green computing and environmental computing perspective, the total time from model conception to final model deployment is interesting.\r\n\r\n"
}
