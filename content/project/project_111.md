{
  "Title": "Physiological Signal Classification",
  "link_to_issue": "https://github.com/brainhackorg/global2021/issues/111",
  "issue_number": 111,
  "labels": [
    {
      "name": "programming:Julia",
      "description": "",
      "color": "5319e7"
    },
    {
      "name": "topic:physiology",
      "description": "",
      "color": "006b75"
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
      "name": "modality:ECG",
      "description": "",
      "color": "1d76db"
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
  "content": "**Project title:**\r\nPhysiological Signal Classification\r\n\r\n**Leader:**\r\nDavid Romero-Bascones (@drombas)\r\n\r\n**Collaborators:**\r\nStefano Moia\r\n\r\n**Topic:**\r\nMachine learning, Physiology, Time-series analysis\r\n\r\n**Project description:**\r\nPhysiopy is is a python3 suite to format and analyse physiological recordings. One of the current development goals is to implementing an automatic signal classificator that, given a signal as input, is be able to determine the type of the signal.In this project we provide time-series data of 4 kinds of physiological signals (cardiac, respiratory chest, O2 and CO2) and the goal will be to collaborate to find robust features that allow discerning between them.\r\n\r\n**Data to use:**\r\nData to be used:\r\n- 4 type of signals (cardiac, respiratory chest, O2 and CO2)- 240 time-series (60x4) recordings of 500 seconds long\r\n- 2 files: time_series.csv (time-series data) and annotations.csv (time-series labels)\r\n\r\nLink: https://www.dropbox.com/sh/3y5lhpn09qiz4my/AABKmpFuaGP_aHqxsAJ6LVwza?dl=0\r\n\r\n**Link to project repository:**\r\nhttps://github.com/drombas/BHD-physiological-classification\r\n\r\n**Goals for Brainhack Donostia 2021:**\r\nEasy:\r\n- Develop a classifier between cardiac and respiratory signals (O2,CO2,chest)\r\nDoable but harder:\r\n- Develop a classifier between all four signals\r\nOptimistic:\r\n- Integrate the classifier into the development branch\r\n\r\n**First tasks:**\r\nThe project has 3 phases:\r\n1. Exploration: download the data and visualize several signals to get an idea of how they look like.\r\n2. Feature engineering: try to find features that discern the signals (using any programming language). You can create features:\r\n  - By hand: coming up with features based on intuition (we already have some ideas)\r\n  - Automatically with approaches like HCTSA (https://github.com/benfulcher/hctsa)\r\n3. Implementation: build the final classification pipeline in Python with the best features.\r\n\r\n**Communication channels:**\r\nhttps://mattermost.brainhack.org/brainhack/channels/physiopy\r\n\r\n**Video channel:**\r\nZoom\r\n\r\n**Number of collaborators:**\r\nMore\r\n\r\n**Credit to collaborators:**\r\nPhysiopy adopts the all-contributors system to recognise contributions. Contributors will be recognised as such in the relevant library README and as authors during outreach (conference posters, talks, ...).\r\n\r\n**Type of project:**\r\nCoding methods, Method development\r\n\r\n**Development status:**\r\nConcept but no content\r\n\r\n**Programming languages:**\r\nJulia, Matlab, Python, R\r\n\r\n**Necessary Programming skills level for the project:**\r\nFamiliar\r\n\r\n**Necessary git skills level for the project:**\r\nNone\r\n\r\n**Modality:**\r\nECG, physiology\r\n\r\n**Software suites:**\r\nphysiopy\r\n\r\n**Email:**\r\ndavidrb093g@gmail.com\r\n\r\n**What will participants learn:**\r\nBasic time-series processing (normalization, filtering, maxima location, ...). \r\nTime-series classification (feature engineering, validation, ...)."
}