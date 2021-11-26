{
  "Title": "Universal data load for neural networks",
  "link_to_issue": "https://github.com/brainhackorg/global2021/issues/109",
  "issue_number": 109,
  "labels": [
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
      "name": "tools:MNE",
      "description": "",
      "color": "0052cc"
    },
    {
      "name": "programming:Python",
      "description": "",
      "color": "5319e7"
    },
    {
      "name": "tools:Nipype",
      "description": "",
      "color": "0052cc"
    },
    {
      "name": "modality:EEG",
      "description": "",
      "color": "1d76db"
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
      "name": "bhg:donostia_esp_1",
      "description": "BHG 2021 Donostia event",
      "color": "d4c5f9"
    }
  ],
  "content": "**Project title:**\r\nUniversal data load for neural networks\r\n\r\n**Leader:**\r\nNing Mei (@nmningmei)\r\n\r\n**Collaborators:**\r\n\r\n\r\n**Topic:**\r\nDeep learning, Input/Output\r\n\r\n**Project description:**\r\nThere exist data loader pipeline for deep neural network project using Tensorflow or Pytorch, but they mainly focus on computer visions and natural language processing. When neuroscientists implement deep neural network models on neuroimaging or neurosignal data, a customized pipeline must be written from scratch every time. This project aims to provide a universal data loader, based on either Tensorflow or Pytorch data loader pipelines, so that it is easier for neuroscientists to implement neural network modeling in the next steps. \r\n\r\n**Data to use:**\r\nData is to be determined but one M/EEG and one fMRI data will be selected for testing.\r\n\r\n**Link to project repository:**\r\n\r\n\r\n**Goals for Brainhack Donostia 2021:**\r\n\r\n1. A data loader for Numpy arrays\r\n\r\n2. A data loader for converting EEG Epochs data to batches3. A data loader for converting fMRI data to batches\r\n\r\n**First tasks:**\r\n\r\n1. https://github.com/nmningmei/BOLD5000_autoencoder/blob/master/scripts/2.2.extract%20volumes.py\r\n\r\n2. https://github.com/nmningmei/BOLD5000_autoencoder/blob/master/scripts/3.1.simple%20autoencoder%202D.py#L25:L39\r\n\r\n**Communication channels:**\r\n\r\n\r\n**Video channel:**\r\nJitsi\r\n\r\n**Number of collaborators:**\r\n3\r\n\r\n**Credit to collaborators:**\r\nN/A\r\n\r\n**Type of project:**\r\nData management, Documentation, Pipeline development\r\n\r\n**Development status:**\r\nBasic structure\r\n\r\n**Programming languages:**\r\nPython\r\n\r\n**Necessary Programming skills level for the project:**\r\nIntermediate\r\n\r\n**Necessary git skills level for the project:**\r\nFamiliar\r\n\r\n**Modality:**\r\nEEG, fMRI\r\n\r\n**Software suites:**\r\nMNE, Nipype\r\n\r\n**Email:**\r\nnmei@bcbl.eu\r\n\r\n**What will participants learn:**\r\n1. Object oriented programming in Python\r\n2. Knowledge about arrays and tensors\r\n3. Basic I/O knowledge of M/EEG (MNE-python) and fMRI (nibabel)"
}