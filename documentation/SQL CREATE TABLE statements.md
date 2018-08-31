
```
CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(20) NOT NULL, 
	password VARCHAR(30) NOT NULL, 
	email VARCHAR(144), 
	phone VARCHAR(20), 
	PRIMARY KEY (id)
)

CREATE TABLE role (
	id INTEGER NOT NULL, 
	name VARCHAR(50), 
	PRIMARY KEY (id), 
	UNIQUE (name)
)

CREATE TABLE event (
	id INTEGER NOT NULL, 
	type VARCHAR(144) NOT NULL, 
	date DATE NOT NULL, 
	pax INTEGER, 
	info VARCHAR(500), 
	staffed BOOLEAN NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (staffed IN (0, 1))
)

CREATE TABLE account_role (
	account_id INTEGER NOT NULL, 
	role_id INTEGER NOT NULL, 
	PRIMARY KEY (account_id, role_id), 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(role_id) REFERENCES role (id)
)

CREATE TABLE assignment (
	id INTEGER NOT NULL, 
	starttime TIME NOT NULL, 
	endtime TIME NOT NULL, 
	role VARCHAR(144) NOT NULL, 
	event_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(event_id) REFERENCES event (id)
)
CREATE TABLE account_assignment (
	account_id INTEGER NOT NULL, 
	assignment_id INTEGER NOT NULL, 
	regtime DATETIME, 
	confirmed BOOLEAN NOT NULL, 
	PRIMARY KEY (account_id, assignment_id), 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(assignment_id) REFERENCES assignment (id), 
	CHECK (confirmed IN (0, 1))
```
