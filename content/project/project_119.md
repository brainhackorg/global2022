{
  "Title": "Inferring task-related higher-order interactions from brain network signals",
  "link_to_issue": "https://github.com/brainhackorg/global2022/issues/119",
  "issue_number": 119,
  "labels": [
    {
      "name": "modality:behavioral",
      "description": "",
      "color": "1d76db"
    },
    {
      "name": "marseille_fra",
      "description": "Marseille event",
      "color": "d4c5f9"
    },
    {
      "name": "git_skills:0_none",
      "description": "",
      "color": "bfdadc"
    },
    {
      "name": "git_skills:1_commit_push",
      "description": "",
      "color": "bfdadc"
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
      "name": "modality:ECOG",
      "description": "",
      "color": "1d76db"
    },
    {
      "name": "programming:documentation",
      "description": "Markdown, Sphinx",
      "color": "5319e7"
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
      "name": "status:published",
      "description": "",
      "color": "0e8a16"
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
      "name": "topic:information_theory",
      "description": "",
      "color": "006b75"
    }
  ],
  "content": "### Title\r\n\r\nInferring task-related higher-order interactions from brain network signals\r\n\r\n### Leaders\r\n\r\n- Etienne Combrisson (Twitter : @kNearNeighbors)\r\n- Andrea Brovelli (Twitter : @BrovelliAndrea)\r\n\r\n### Collaborators\r\n\r\n- Daniele Marinazzo (Twitter : @dan_marinazzo)\r\n- Matteo Neri\r\n\r\n### Brainhack Global 2022 Event\r\n\r\nBrainhack Marseille\r\n\r\n### Project Description\r\n\r\nA central hypothesis in neuroscience posits that cognitive functions emerge from complex interactions between multiple brain regions. Similarly, cognitive deficits due to trauma or neurological conditions, such as after stroke, crucially depend on network-level alterations that disrupt normal interactions among multiple brain areas. Although central, progress towards testing these hypotheses has been limited by the lack of approaches for studying interactions between multiple brain regions beyond pairwise relations, the so-called higher-order interactions (HOIs). The aim of our project is to build a novel approach based on recent advances in information theory (the O-information metric) to infer task- or condition-specific HOIs (functional HOIs) from brain signals. We will explore the possibility to combine O-information estimates with permutation-based statistics implemented in [Frites](https://github.com/brainets/frites)\r\n\r\n### Link to project repository/sources\r\n\r\n# Toolboxes\r\n\r\n- [HOI toolbox 2021](https://github.com/brainets/hoi_bhk)\r\n- [Frites](https://github.com/brainets/frites)\r\n\r\n# Papers\r\n\r\n-  [Rosas et al. 2019](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.100.032305) \r\n- [Stramaglia et al. 2021](https://www.frontiersin.org/articles/10.3389/fphys.2020.595736/full)\r\n\r\n### Goals for Brainhack Global\r\n\r\nThe main goal of this BrainHack is to have a working first version of the task-related HOI\r\n\r\n### Good first issues\r\n\r\n1. Prototype the main function (i.e. define input and output types, write down important internal steps)\r\n2. Make it works in the non-dynamic case\r\n3. Investigate the use of [Jax](https://github.com/google/jax) to speed up computations\r\n4. Be able to simulate data with a known amount of redundancy and synergy\r\n\r\n### Communication channels\r\n\r\n[TO BE ADDED]\r\n\r\n### Skills\r\n\r\nComputational : 70%\r\nInformation-theory : 60%\r\nMath : 50%\r\nPython : 70%\r\n\r\n### Onboarding documentation\r\n\r\n_No response_\r\n\r\n### What will participants learn?\r\n\r\nThey will learn about : \r\n- Information-theoretic terminology (redundancy, synergy, mutual information, entropy)\r\n- Conceptual differences between pairwise and higher-order interactions\r\n- Non-parametric statistics\r\n\r\n### Data to use\r\n\r\n_No response_\r\n\r\n### Number of collaborators\r\n\r\n4\r\n\r\n### Credit to collaborators\r\n\r\nCollaborators will be added to our [Frites' Hall of Fame](https://brainets.github.io/frites/overview/ovw_community.html#authors-and-contributors)\r\n\r\n### Image\r\n\r\n![201880960-8965350b-067f-4079-a64d-b482eb704f36](https://user-images.githubusercontent.com/15892073/202182218-f527ce37-773d-4591-b259-194c8211766d.png)\r\n\r\n\r\n### Type\r\n\r\nmethod_development\r\n\r\n### Development status\r\n\r\n1_basic structure\r\n\r\n### Topic\r\n\r\ninformation_theory\r\n\r\n### Tools\r\n\r\nother\r\n\r\n### Programming language\r\n\r\nPython\r\n\r\n### Modalities\r\n\r\nbehavioral, ECOG, EEG, MEG\r\n\r\n### Git skills\r\n\r\n0_no_git_skills, 1_commit_push\r\n\r\n### Anything else?\r\n\r\n_No response_\r\n\r\n### Things to do after the project is submitted and ready to review.\r\n\r\n- [ ] Add a comment below the main post of your issue saying: `Hi @brainhackorg/project-monitors my project is ready!`\r\n- [ ] Twitter-sized summary of your project pitch.",
  "project_description": "\r\n\r\nA central hypothesis in neuroscience posits that cognitive functions emerge from complex interactions between multiple brain regions. Similarly, cognitive deficits due to trauma or neurological conditions, such as after stroke, crucially depend on network-level alterations that disrupt normal interactions among multiple brain areas. Although central, progress towards testing these hypotheses has been limited by the lack of approaches for studying interactions between multiple brain regions beyond pairwise relations, the so-called higher-order interactions (HOIs). The aim of our project is to build a novel approach based on recent advances in information theory (the O-information metric) to infer task- or condition-specific HOIs (functional HOIs) from brain signals. We will explore the possibility to combine O-information estimates with permutation-based statistics implemented in [Frites](https://github.com/brainets/frites)\r\n\r\n"
}
