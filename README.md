![Logo](docs/assets/logo.png)

Fork
=======
This fork modifies some base images to be compatible with raspberry pi.

Instructions for use:
Copy docker-compose.yml.sample to docker-compose.yml
Copy .env.sample to .env
Modify .env for your own requirements
If using SSL certificates, you should pre-create the volume 'certs' and 
add the relevant cert.pem and key.pem files to the root of that volume.
Build & bring up all images with docker-compose up (-d for background mode)

Original Readme
=======

Mailu is a simple yet full-featured mail server as a set of Docker images.
It is free software (both as in free beer and as in free speech), open to
suggestions and external contributions. The project aims at providing people
with an easily setup, easily maintained and full-featured mail server while
not shipping proprietary software nor unrelated features often found in
popular groupware.

Most of the documentation is available on our [Website](https://mailu.io),
you can also [try our demo server](https://mailu.io/master/demo.html)
before setting up your own, and come [talk to us on Matrix](https://matrix.to/#/#mailu:tedomum.net).

Features
========

Main features include:

- **Standard email server**, IMAP and IMAP+, SMTP and Submission
- **Advanced email features**, aliases, domain aliases, custom routing
- **Web access**, multiple Webmails and adminitration interface
- **User features**, aliases, auto-reply, auto-forward, fetched accounts
- **Admin features**, global admins, announcements, per-domain delegation, quotas
- **Security**, enforced TLS, Letsencrypt!, outgoing DKIM, anti-virus scanner
- **Antispam**, auto-learn, greylisting, DMARC and SPF
- **Freedom**, all FOSS components, no tracker included

![Domains](docs/assets/screenshots/domains.png)

Contributing
============

Mailu is free software, open to suggestions and contributions. All
components are free software and compatible with the MIT license. All
specific configuration files, Dockerfiles and code are placed under the
MIT license.
