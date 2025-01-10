# EditorCrew
> EditorCrew is an AI Agent Crew that makes use of multiple model providers to generate polished articles.


## Demo 

<video src="https://github.com/user-attachments/assets/a1da76bf-719b-4d05-a158-820bbcf32654"></video>


## 🤖 Model Architecture

EditorCrew leverages four powerful LLMs, each specialized for different aspects of content creation:

- Content Writer from Groq  
- Critic from Sambanova  
- Editor from Google Gemini  
- Rater from Cerebras


1. **Content Writer**: `groq/llama-3.1-70b-versatile`
   - 70B parameter model
   - Specialized in versatile content generation
   - Creates engaging, well-structured initial drafts

2. **Content Critic**: `sambanova/Meta-Llama-3.1-8B-Instruct`
   - 8B parameter model
   - Expert in content analysis
   - Provides detailed, constructive feedback

3. **Content Editor**: `gemini/gemini-2.0-flash-exp`
   - Latest Gemini model
   - Specialized in content refinement
   - Implements improvements while maintaining content integrity

4. **Content Rater**: `cerebras/llama3.1-70b`
   - 70B parameter model
   - Expert in content evaluation
   - Provides comprehensive quality assessment

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/editorcrew.git
cd editorcrew

# Install dependencies
pip install -r requirements.txt

# Set up your API keys or add a .env file
export GROQ_API_KEY="your-groq-key"
export SAMBANOVA_API_KEY="your-sambanova-key"
export GEMINI_API_KEY="your-gemini-key"
export CEREBRAS_API_KEY="your-cerebras-key"
```

## 💻 Usage

```python
# edit the topic of interest in main.py
crewai run
```

## 📊 Output Structure

The system generates several files during the process:
- `original_article.md`: Original content
- `article_critique.md`: Detailed feedback
- `improved_article.md`: Enhanced version
- `article_rating.md`: Quality assessment report

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License
