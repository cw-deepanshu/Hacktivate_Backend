# Setup

## 1. Clone the repository:
   ```sh
   git clone <repository_url>
  ```
## 2. Installing dependencies in `Hacktivate_Backend`:
   ```sh
   cd Hacktivate_Backend
   npm i
   ```
## 3. Setup for Analyser
### Navigate inside Analyser directory
  ```sh
   cd Analyser
   ```
### Setting Up Spacy
  ```sh
  pip install -U pip setuptools wheel
  pip install -U 'spacy[transformers,lookups]'
  python -m spacy download en_core_web_lg
   ```
### Installing all the requirements
  ```sh
   pip install -r .\requirements.txt
   ```
### Creating Training Data
#### This may take few minutes
  ```sh
   python -m spacy train config.cfg --output ./ --paths.train ./train.spacy --paths.dev ./train.spacy
   ```
## 4. Installing dependecies in `Hacktivate_Frontend`:
   ```sh
   cd Hacktivate_Frontend
   npm i
   ```
## 5. Run the backend and frontend in the localhost
### Backend
  ```sh
   cd Hacktivate_Backend
   npm start
   ```
### Frontend
  ```sh
   cd Hacktivate_Frontend
   npm start
   ```
# Flow

![Flow](https://github.com/cw-deepanshu/Hacktivate_Backend/assets/155448333/31f64158-75f7-4471-8f45-2480c3c4c1f4)
