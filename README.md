# gemini_chat_bot
Flex Python app for chat with Gemini

## Deployment Process
Deployment involves setting up the cloud instance, installing dependencies, and configuring the application. For GCP:

Create a new project in the GCP console and enable the Gemini API at GCP API Library.
Generate an API key at GCP API Keys and set it as an environment variable.
Launch a Compute Engine instance (e.g., e2-micro) with Ubuntu, install Python and pip, and install google-generativeai and flask.
Upload the source code, set the GEMINI_API_KEY environment variable, and run the Flask app, ensuring port 80 is open via firewall rules.
Note the public IP address for API access, available by default with the instance.
For AWS, the process is similar:

Launch an EC2 instance (e.g., t2.micro) with Ubuntu, and configure security groups to allow port 80 traffic.
Install dependencies and deploy the application as above, setting the API key and running the Flask app.
Obtain the public IP for external access, assigned by default.
Both deployments ensure the API is publicly accessible, with costs monitored to stay within budget, given the small instance types selected.
