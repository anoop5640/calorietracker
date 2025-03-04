# Calorie Tracker Application

## Overview
The **Calorie Tracker Application** is a cloud-based web application designed to help users track and manage their daily nutrition intake. It provides access to the calorie content of food items consumed by users using a **Calorie API** developed with Django REST Framework. The application leverages **microservices architecture** to ensure scalability, robustness, and independent scaling of services. 

The application integrates three APIs:
1. **Calorie API**: Provides calorie information for food items.
2. **Recipe Suggestion API**: Suggests recipes based on user-provided ingredients.
3. **Calorie Recommendation API**: Recommends daily calorie intake based on user height and weight.

The application is deployed on **AWS Elastic Beanstalk**, utilizing cloud-native design principles for automated resource allocation, load balancing, and scaling.

---

## Features
- **Calorie Tracking**: Users can track their daily calorie intake using the Calorie API.
- **Recipe Suggestions**: Users can get recipe suggestions based on available ingredients.
- **Calorie Recommendations**: Users receive personalized calorie intake recommendations based on their height and weight.
- **Microservices Architecture**: Independent scaling of services for better performance and reliability.
- **Cloud-Native Design**: Automated resource allocation, load balancing, and scaling using AWS Elastic Beanstalk.

---

## Technologies Used
- **Backend**: Python, Django, Django REST Framework
- **Frontend**: HTML, CSS, JavaScript 
- **APIs**:
  - Calorie API (developed by me)
  - Recipe Suggestion API (developed by colleagues)
  - Calorie Recommendation API (developed by colleagues)
- **Cloud Deployment**: AWS Elastic Beanstalk
- **Database**: SQLite/PostgreSQL (or any database used)
- **Version Control**: Git, GitHub
  
---

## Architecture
The application follows a **microservices architecture**, with each API functioning as an independent service. This allows for:
- **Independent Scaling**: Each service can be scaled independently based on demand.
- **Fault Isolation**: Issues in one service do not affect others.
- **Ease of Maintenance**: Services can be updated or replaced without impacting the entire application.


## Setup Instructions
Follow these steps to set up the project locally:

### Prerequisites
- Python 3.x
- Django
- Django REST Framework
- AWS CLI (for deployment)
- Git

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/calorie-tracker-app.git
   cd calorie-tracker-app
