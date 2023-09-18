# django-email-campaign

This Django-based email campaign application provides a backend API for managing and executing email campaigns. With features for creating campaigns, scheduling deliveries, and tracking email delivery status, it simplifies the process of conducting email marketing campaigns.

## Table of Contents

* [Features](#features)
* [Installation](#installation)
* [Usage](#usage)
* [API Endpoints](#api-endpoints)
* [Authentication](#authentication)
* [Database](#database)
* [Scheduled Email Sending](#scheduled-email-sending)

## Features

- User authentication using [Django Rest Framework (DRF)](https://www.django-rest-framework.org/)
- JWT authentication with [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/)
- Create and manage email campaigns
- Schedule email campaigns for future delivery
- Bulk email sending to specified recipients
- **Emails sent using File Backend (configured for development)**
- **Email tracking not implemented (see [Email Tracking](#email-tracking))**
- Asynchronous email sending using [DjangoQ](https://django-q.readthedocs.io/)
- Scrapping emails from [email_scrapping](https://github.com/your-username/email_scrapping) app

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/django-email-campaign.git
   
