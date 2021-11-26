{
  "Title": "Data Driven Spiking Neural Network Optimization in Julia",
  "link_to_issue": "https://github.com/brainhackorg/global2021/issues/98",
  "issue_number": 98,
  "labels": [
    {
      "name": "git_skills:0_none",
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
      "name": "topic:physiology",
      "description": "",
      "color": "006b75"
    },
    {
      "name": "topic:neural_networks",
      "description": "",
      "color": "006b75"
    },
    {
      "name": "topic:single_neuron_models",
      "description": "",
      "color": "006b75"
    },
    {
      "name": "project_development_status:1_basic structure",
      "description": "",
      "color": "bfd4f2"
    },
    {
      "name": "topic:data_visualisation",
      "description": "",
      "color": "006b75"
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
      "name": "programming:R",
      "description": "",
      "color": "5319e7"
    },
    {
      "name": "topic:reproducible_scientific_methods",
      "description": "",
      "color": "006b75"
    },
    {
      "name": "programming:Python",
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
      "name": "git_skills:2_branches_PRs",
      "description": "",
      "color": "bfdadc"
    },
    {
      "name": "git_skills:3_continuous_integration",
      "description": "",
      "color": "bfdadc"
    },
    {
      "name": "project_type:visualisation",
      "description": "",
      "color": "c5def5"
    }
  ],
  "content": "### Title\r\n\r\nData-Driven Spiking Neural Network Optimization in Julia\r\n\r\n### Leaders\r\n\r\nRussell Jarvis\r\n@rjjarvis (mattermost)\r\n@russelljjarvis (github)\r\n\r\n### Collaborators\r\n\r\nSeeking collaborators\r\n\r\n### Brainhack Global 2021 Event\r\n\r\nBrainhack Australasia\r\n\r\n### Project Description\r\n\r\n### What are you doing, for whom, and why?\r\n\r\n- The project is for everyone who wants to try to do data fitting of neuron models **without** Python+external simulation tools. The project is for people who have been **frustrated** by writing support code in Python for externally supported simulator tools, and who would like to see efficient cellular and network data fitting happening all inside one language.\r\n\r\n- The project intends to consolidate neural electro-physiology tools and support that have existed in Julia for a while by applying tools by example.\r\n\r\n### What makes your project special and exciting?\r\nIt has a basis in Julia-lang which might be novel and exciting for many people, yet, the scope of the project is meta-package, meaning that many of the goals of the project are beginner-friendly.\r\n\r\n### How to get started?\r\n\r\n`git clone https://github.com/russelljjarvis/SpikeNetOpt.jl`\r\n\r\nData fitting a spiking neural network by exploring the effect of the parameter that controls connectome graph structure:\r\n\r\n```\r\ncd examples\r\njulia sdo_network.jl\r\n```\r\n\r\nSingle cell data fitting against spike times:\r\n\r\n```\r\ncd test\r\njulia single_cell_opt_adexp.jl \r\njulia single_cell_opt_izhi.jl\r\n```\r\n### Where to find key resources?\r\n\r\n\r\n### Link to project repository/sources\r\n\r\nhttps://github.com/russelljjarvis/SpikeNetOpt.jl\r\n\r\n### Goals for Brainhack Global\r\n\r\n* Refactor optimizer design from bespoke specific examples to a general user interface. \r\n* Benchmarking of three different Julia Spiking Neural Network backend simulator speeds.\r\n* eliminate global variables and untyped variables.\r\n\r\n### Good first issues\r\n\r\n1. Most fun issue: Benchmark execution speed and memory consumption for similar-sized networks on the same network models, for different Julia SNN backends.\r\nThese three approaches need to openly be battled out, against each other for execution speed and memory efficiency.\r\n* https://github.com/AStupidBear/SpikingNeuralNetworks.jl\r\n* https://github.com/leaflabs/WaspNet.jl\r\n* https://github.com/darsnack/SpikingNN.jl\r\n\r\n2. [Make package installable via Project.toml, etc.](https://github.com/russelljjarvis/SpikeNetOpt.jl/issues/3)\r\n\r\n3. Refactor optimizer design from bespoke specific examples to a general user interface. \r\n\r\n4. Make scatter plot animation of optimizer succeeding.\r\n\r\n5. Use existing Python/BluePyOpt code to draw the GA evaluated error surface.\r\n\r\nProperly cite this code and borrow from BPO /notebook here:\r\nhttps://github.com/BlueBrain/BluePyOpt/blob/master/examples/simplecell/simplecell-paperfig.ipynb\r\nPython code Cell 26 draws the error surface.\r\n\r\n6. Convert Python Sciunit relative difference score to Julia relative difference score.\r\n\r\nSciunit scoring has tools, for scaling and normalizing feature measurements, some of these are trivial and some are elaborate.\r\nhttps://github.com/scidash/sciunit/blob/master/sciunit/scores/complete.py#L247-L329 \r\n\r\nImplement in Julia sciunits RelativeDifferenceScore, naming convention, and implementation. Note Julia is not Object orientated, so skip over Python's inheritance, if it seems necessary to use a container use Julia struct. It might be helpful to re-implement multiple sciunit scores in Julia, but the most immediately useful one is RelativeDifferenceScore\r\n\r\n### Communication channels\r\n\r\nhttps://mattermost.brainhack.org/brainhack/channels/spikenetoptjl\r\n\r\n### Skills\r\n\r\n- git push/pull\r\n- git commit \r\n- git PR\r\n- A desire to learn Julia (but with pre-existing programming knowledge)\r\n\r\n### Onboarding documentation\r\n\r\nI will create a contributing.md in the interim.\r\n\r\n### What will participants learn?\r\n\r\n* Julia package management of projects.\r\n* Julia structs\r\n* Julia multiple dispatch\r\n* Julia typing\r\n\r\n### Data to use\r\n\r\nAt the moment single-cell model fitting occurs on Allen Brain Observatory data (these are cached in JLD files), I have written a Python API included in the Julia code repository (python is called from Julia). \r\n\r\nThis project would really benefit from experimental multicellular spike train data.\r\n\r\nhttps://observatory.brain-map.org/visualcoding/sdk/index\r\n\r\n### Number of collaborators\r\n\r\n5\r\n\r\n### Credit to collaborators\r\n\r\nI have started using the all contributors tool which makes all contributions to the repository visible (including raising issues via GitHub, or even ideas conveyed outside of GitHub). Also, I can write a reference letter for substantive contribution.\r\n\r\nhttps://github.com/all-contributors/all-contributors\r\n\r\n\r\n### Image\r\n\r\nhttps://user-images.githubusercontent.com/7786645/142357325-60ffea1c-5ef1-4553-a392-7530792cfba0.png\r\n\r\n### Caption\r\n\r\nWhy Julia? Python package management is already complicated, reproducible model optimization is made worse by combining Python with external simulators.\r\n\r\nImage source: https://xkcd.com/1987/\r\n\r\n### Type\r\n\r\ncoding_methods, documentation, method_development, visualization\r\n\r\n### Development status\r\n\r\n1_basic structure\r\n\r\n### Topic\r\n\r\ndata_visualisation, neural_networks, reproducible_scientific_methods, single_neuron_models, other\r\n\r\n### Tools\r\n\r\nPython space: \r\nNetworkUnit, NeuronDataWithoutBorders, Neo Analog Signal. (note to be pragmatic, this project still uses some Python)\r\n\r\nJulia space: \r\nClearStacktrace.jl (makes error messages much easier to read)\r\nSignalAnalysis.jl, Evolutionary.jl, SpikingNeuralNetworks.jl, SpikeSynchrony.jl, PyCall.jl\r\n\r\n### Programming language\r\n\r\nJulia, Python.\r\n\r\n### Modalities\r\n\r\nother\r\n\r\n### Git skills\r\n\r\n0_no_git_skills, 1_commit_push, 2_branches_PRs, 3_continuous_integration\r\n\r\n### Anything else?\r\n\r\nAlthough some Python is used to corroborate/validate optimized models, crucially no Python is used in the optimization loops, as calling Python with PyCall is not fast.\r\n\r\n### Things to do after the project is submitted.\r\n\r\n\r\n# Twitter sized summary\r\n\r\nJulia has enough tools to support fitting spiking neural network models to data. Python speed necessitates external simulators to do network simulation. It would be more developer-friendly to do fast, efficient data fitting of spike trains to network models in one language, let us try to do that here.",
  "project_url": "https://github.com/russelljjarvis/SpikeNetOpt.jl",
  "project_description": "\r\n\r\n"
}
