{
  "Title": "Going beyond pairwise interactions by digging into Higher-Order Interactions",
  "link_to_issue": "https://github.com/brainhackorg/global2021/issues/133",
  "issue_number": 133,
  "labels": [
    {
      "name": "programming:documentation",
      "description": "Markdown, Sphinx",
      "color": "5319e7"
    },
    {
      "name": "status:published",
      "description": "",
      "color": "0e8a16"
    },
    {
      "name": "project_development_status:1_basic structure",
      "description": "",
      "color": "bfd4f2"
    },
    {
      "name": "project_tools_skills:familiar",
      "description": "",
      "color": "c2e0c6"
    },
    {
      "name": "project",
      "description": "",
      "color": "f9bc70"
    },
    {
      "name": "programming:Matlab",
      "description": "",
      "color": "5319e7"
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
      "name": "topic:information_theory",
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
      "name": "bhg:marseille_fra_1",
      "description": "BHG 2021 Marseille event",
      "color": "d4c5f9"
    }
  ],
  "content": "### Title\n\nGoing beyond pairwise interactions by digging into Higher-Order Interactions\n\n### Leaders\n\nEtienne Combrisson (@EtienneCmb), Andrea Brovelli (@brovelli) and Daniele Marinazzo (@danielemarinazzo)\n\n### Collaborators\n\n_No response_\n\n### Brainhack Global 2021 Event\n\nBrainhack Marseille\n\n### Project Description\n\nModern theories suggest that cognitive functions emerge from the dynamic coordination of neural activity over large-scale and hierarchical networks. Currently, the characterization of a network and therefore, the functional interactions between brain regions, is usually performed using metrics of Functional Connectivity (FC). FC analysis is mostly based on the quantification of statistical relations between pairs of brain regions. However, pairwise interactions are probably insufficient to explain the emergence of more complex brain network interactions, such as during goal-directed learning tasks. Here, we propose to move beyond pairwise interactions by studying at Higher Order Interactions (HOI) i.e. quantifying the information carried by groups of \"over-two\" brain regions (= multiplets). As a first step, a framework called O-information (= Information about Organizational structure) was recently proposed to characterize redundancy- and synergy-dominated systems. This framework has recently been extended with the dOinfo (= dynamic Information about Organizational structure) to quantify how multiplets of variables carry information about the future of the dynamical system they belong to. This dOinfo extension allows to separate multiplets of variables which influence synergistically the future of the system from redundant multiplets.\r\n\r\nSince (d)OInfo frameworks are recent, the math underneath are quite new and we are not necessary familiar with it. The overall goal of this project is to understand the methods by looking at the reference papers and the Python / Matlab implementations of both (d)OInfo.\n\n### Link to project repository/sources\n\nhttps://github.com/PranavMahajan25/HOI_toolbox\n\n### Goals for Brainhack Global\n\nDuring this BainHack, we will :\r\n1. Go through the reference papers (i.e. [Rosas et al. 2019](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.100.032305) and [Stramaglia et al. 2021](https://www.frontiersin.org/articles/10.3389/fphys.2020.595736/full)) to build an intuition of the math undergoing the HOI\r\n2. Go through the Python toolbox [HOI_toolbox](https://github.com/PranavMahajan25/HOI_toolbox) to understand what are the input / output types, to identify the main accessible functions such as understanding the internals\r\n3. Make the package easy to install, probably clean up so files\r\n4. Identify whether there are coding bottlenecks that could be easily solved to speed up computations (soft Numba, multi-core, tensor-computations etc.)\r\n\r\nIf we still have time, here are some new features that could be added to the Python toolbox :\r\n1. Implementation of false discovery rate for the significance of the multiplets\r\n2. Speed up of the bootstrap\r\n3. Include some plotting functions\n\n### Good first issues\n\n1. issue one: how to move progressively away from pairwise interactions\r\n\n\n### Communication channels\n\nhttps://mattermost.brainhack.org/brainhack/channels/bhk_hoi\n\n### Skills\n\nComputational : 70%\r\nInformation-theory : 60%\r\nMath : 50%\r\nPython : 70%\r\nMatlab : 30%\n\n### Onboarding documentation\n\n_No response_\n\n### What will participants learn?\n\n- Concepts like redundant and synergistic information\r\n- Oinfo and dOinfo\r\n- Overall, the math underneath some parts of the information-theory\n\n### Data to use\n\n_No response_\n\n### Number of collaborators\n\n3\n\n### Credit to collaborators\n\nContributors will be added to the README\n\n### Image\n\n![doinfo](https://user-images.githubusercontent.com/15892073/143055839-8f85b60b-b94f-4bc4-8c88-ecaf35f724f2.png)\n\n### Type\n\ncoding_methods\n\n### Development status\n\n1_basic structure\n\n### Topic\n\ninformation_theory\n\n### Tools\n\nother\n\n### Programming language\n\nPython\n\n### Modalities\n\nnot_applicable\n\n### Git skills\n\n1_commit_push\n\n### Anything else?\n\n_No response_\n\n### Things to do after the project is submitted.\n\n- [ ] Add a comment saying: `Hi @Brainhack-Global/project-monitors: my project is ready!`\n- [ ] Twitter-sized summary of your project pitch.",
  "project_url": "https://github.com/PranavMahajan25/HOI_toolbox",
  "project_description": "\n\nModern theories suggest that cognitive functions emerge from the dynamic coordination of neural activity over large-scale and hierarchical networks. Currently, the characterization of a network and therefore, the functional interactions between brain regions, is usually performed using metrics of Functional Connectivity (FC). FC analysis is mostly based on the quantification of statistical relations between pairs of brain regions. However, pairwise interactions are probably insufficient to explain the emergence of more complex brain network interactions, such as during goal-directed learning tasks. Here, we propose to move beyond pairwise interactions by studying at Higher Order Interactions (HOI) i.e. quantifying the information carried by groups of \"over-two\" brain regions (= multiplets). As a first step, a framework called O-information (= Information about Organizational structure) was recently proposed to characterize redundancy- and synergy-dominated systems. This framework has recently been extended with the dOinfo (= dynamic Information about Organizational structure) to quantify how multiplets of variables carry information about the future of the dynamical system they belong to. This dOinfo extension allows to separate multiplets of variables which influence synergistically the future of the system from redundant multiplets.\r\n\r\nSince (d)OInfo frameworks are recent, the math underneath are quite new and we are not necessary familiar with it. The overall goal of this project is to understand the methods by looking at the reference papers and the Python / Matlab implementations of both (d)OInfo.\n\n"
}