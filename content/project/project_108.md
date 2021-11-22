{
  "Title": "Automatic plosive detection and VOT extraction using the Plosion index",
  "link_to_issue": "https://github.com/brainhackorg/global2021/issues/108",
  "issue_number": 108,
  "labels": [
    {
      "name": "tools:Jupyter",
      "description": "",
      "color": "0052cc"
    },
    {
      "name": "project",
      "description": "",
      "color": "f9bc70"
    },
    {
      "name": "status:web_ready",
      "description": "",
      "color": "0e8a16"
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
      "name": "bhg:donostia_esp_1",
      "description": "BHG 2021 Donostia event",
      "color": "d4c5f9"
    }
  ],
  "content": "**Project title:**\r\nAutomatic plosive detection and VOT extraction using the Plosion index\r\n\r\n**Leader:**\r\nFlorent Dueme (@Florent-Dueme)\r\n\r\n**Collaborators:**\r\n??\r\n\r\n**Topic:**\r\nLanguage\r\n\r\n**Project description:**\r\nDo you wish you didn't have to spend hours manually combing through your audio data to identify plosives and extract their voice onset times (VOT)? Introducing the Plosion Index! The Plosion index is a measurement from the speech recognition literature (Ananthapadmanabha, Prathosh, & Ramakrishnan; 2014) to facilitate the detection of plosives in natural language data. It is based on an algorithm that calculate at each time point the ratio between the instantaneous amplitude of an acoustic signal and the mean amplitude of the signal during the preceding few milliseconds. It is designed to detect brutal changes in amplitude typically linked to the puff of air expulsed out of the mouth during the release phase of a plosive. This mean that the Plosive index is not only able to detect plosives in speech data, but also to determine the exact moment of the plosive release, making it possible to automatize the calculation of VOT, that is the interval of time between the release of the plosive and the moment when the vocal chords start to vibrate to produce the following vowel.\r\n\r\n**Data to use:**\r\nSome of my own (Florent) data is available to start working on the project, but my data is overwhelmingly constituted of Spanish and French words and pseudowords starting with the voiced plosive /b/. It would be good to have more data to generalize this technique to other phonemes, especially unvoiced and aspirated plosives, and to plosives in non-initial position.\r\n\r\n**Link to project repository:**\r\nhttps://github.com/Florent-Dueme/Extracting_VOT_with_Plosion_index.git\r\n\r\n**Goals for Brainhack Donostia 2021:**\r\nI have already implemented this algorithm to successfully automatize the extraction of VOT for word-initial prevoiced plosives (such as /b/). The success rate is around 80 to 90%, so some manual verification is still needed. The goal of this project is to build a roadmap to extend the use of this algorithm to non-prevoiced and aspirated plosives, both in word-initial position and inside words, and to improve the efficiency of the algorithm.\r\n\r\n**First tasks:**\r\n- Implement a way to recognize vowel onset (probably using acoustic amplitude in frequencies between 100 and 400 Hz corresponding to the Fondamental frequency of the vochal chords). - Implement a way to use the Plosion index to automatically detect the presence of plosives of a certain type in natural speech data.\r\n\r\n**Communication channels:**\r\n\r\n\r\n**Video channel:**\r\nZoom\r\n\r\n**Number of collaborators:**\r\n4\r\n\r\n**Credit to collaborators:**\r\nAll contributors will get credit for their work on the README file.\r\n\r\n**Type of project:**\r\nPipeline development\r\n\r\n**Development status:**\r\nBasic structure\r\n\r\n**Programming languages:**\r\nPython, Praat\r\n\r\n**Necessary Programming skills level for the project:**\r\nFamiliar\r\n\r\n**Necessary git skills level for the project:**\r\nNone\r\n\r\n**Modality:**\r\nBehavioral\r\n\r\n**Software suites:**\r\nJupyter\r\n\r\n**Email:**\r\nf.dueme@bcbl.eu\r\n\r\n**What will participants learn:**\r\nWe will learn how to:\r\n\r\n* do research in collaborative on open source projects.\r\n* develop a pipeline, from its conceptualization till development.\r\n* Perform acoustic signal processing in Python. \r\n* Automatize acoustic analyses. \r\n* Manipulate Praat objects such as TextGrids in Python."
}