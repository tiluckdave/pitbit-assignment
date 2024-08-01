Below is the prompt used for conversion of resume to json format.
The prompt follows CO-STAR prompt engineering technique to get the task done.

# Prompt

```md
# Context

Act as a resume parser. Your job is to parse all the important information from a resume which is provided in image format to you. All the information parsed must be structured properly in JSON format.

# Objective

You must get all the details of the person from the resume and and understand all the headlines available in his/her resume and structure the json data accordingly. For e.g. data in the resume could be name, contact details such as phone number, email id, address, then there can be skills section, projects section, experiences, education, etc and more. Further each section might have details like experiences can have multiple experiences each having company name, job title, durations, skills worked on, description, etc and more. Your task is to identify such details properly and structure them in JSON format

# Style

Keep your style very simple. The response is ONLY a json block which contains the structured resume in JSON format

# Audience

Consider the audience for this chat to be developers who will use the structured resume in json format for further processing

# Response

Be concise, do not halucinate data, do not create any new data, Put the data parsed from the resume as it is without any change.
```

# Output

```json
{
	"name": "Tilak Dave",
	"contact": {
		"phone": "+91 8625996825",
		"email": "tilak.dave22@vit.edu",
		"location": "Pune, India"
	},
	"summary": "Pursuing Computer Engineering with hands-on experience in Full Stack Development, AI, and Blockchain. Able to develop applications and AI solutions. Extensive project work and internships. Winner of national-level hackathons, showcasing strong problem-solving skills and technical expertise.",
	"skills": {
		"languages": ["Java", "Python", "JavaScript", "TypeScript"],
		"artificial_intelligence": [
			"OpenAI",
			"langchain",
			"LLMs",
			"Vectorstores",
			"Machine Learning"
		],
		"full_stack": [
			"React",
			"NextJs",
			"NodeJs",
			"Flask",
			"PostgreSQL",
			"MongoDB",
			"Firebase"
		],
		"others": ["Blockchain", "Solidity", "Git", "GitHub", "AWS"]
	},
	"internships": [
		{
			"title": "Full Stack & AI Developer Intern",
			"company": "AfterQuote",
			"duration": "July 2023 – March 2024",
			"responsibilities": [
				"Developed production-ready SaaS applications using NextJs, TypeScript, and PostgreSQL.",
				"Key projects included rendering of Parsing important details from Email using generative AI, customer portal, and orders & people management systems."
			]
		}
	],
	"projects": [
		{
			"title": "NyaySathi",
			"description": "Legal AI Assistant (NextJs, Flask, OpenAI, Firebase)",
			"details": [
				"Developed a Retrieval Augmented Generation (RAG) on top of LLM model for legal queries.",
				"Created fully functional web & mobile apps with voice i/o capabilities in regional languages.",
				"Implemented OCR technology for legal file summarization in regional languages."
			]
		},
		{
			"title": "Web3lance",
			"description": "Freelance platform on Polygon (NextJs, Polygon, Solidity)",
			"details": [
				"Built the core of a freelancing platform on the blockchain with an escrow contract in Solidity.",
				"Ensured secure transactions using the Matic coin on the Polygon chain."
			]
		},
		{
			"title": "Fast Feedback",
			"description": "Comments on Static Website (NextJs, Firebase, Stripe)",
			"details": [
				"Developed an end-to-end SaaS product for adding comments systems on static sites and blogs.",
				"Managed payment & subscription with Stripe, and used Firebase as the primary database.",
				"Developed API endpoints, dashboard, public pages, and embed tags."
			]
		},
		{
			"title": "Social Credit System",
			"description": "AI based social credit score (Tensorflow, Python, Flask, NextJs)",
			"details": [
				"Designed a system for human identification and behaviour detection using webRTC.",
				"Implemented voice detection and natural language processing for tone analysis.",
				"Calculated social credit scores similar to credit ratings."
			]
		}
	],
	"achievements": [
		"Winner of Smart India Hackathon 2023 (Project Details: NyaySathi - AI Legal Assistant)",
		"Winner of three national level hackathons (HackWeb3Conf, HackOverflow, SheBuilds Hack)",
		"Contributor at SuperteamDAO, Event Manager at TEDxVITPune, Community Moderator at BlueLearn."
	],
	"education": {
		"degree": "B. Tech. in Computer Engineering",
		"graduation_year": "2025",
		"GPA": "8.85",
		"institution": "Vishwakarma Institute of Technology, Pune (Savitribai Phule Pune University)"
	}
}
```
