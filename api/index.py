<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<title>Portfolio - Jeanalen Tabaranza</title>
		<link rel="stylesheet" href="styles.css" />
		<link
			rel="stylesheet"
			href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"
		/>
	</head>
	<body>
		<!-- Navigation Bar -->
		<nav class="navbar">
			<div class="container">
				<div class="navbar-brand">Jeanalen</div>
				<div class="nav-toggle" id="navToggle">
					<span></span>
					<span></span>
					<span></span>
				</div>
				<ul class="nav-menu" id="navMenu">
					<li><a href="#home">Home</a></li>
					<li><a href="#about">About Me</a></li>
					<li><a href="#skills">What I Do</a></li>
					<li><a href="#projects">My Work</a></li>
					<li><a href="#contact">Let's Talk</a></li>
				</ul>
			</div>
		</nav>

		<!-- Hero Section -->
		<section id="home" class="hero">
			<div class="container">
				<div class="hero-content">
					<h1 class="hero-title">Hi, I'm Jeanalen Tabaranza</h1>
					<p class="hero-subtitle">Web Developer & Designer</p>
					<p class="hero-description">
						Creating clean, functional web experiences with modern technologies.
					</p>
					<a href="#projects" class="btn btn-primary">View My Projects</a>
					<a href="#contact" class="btn btn-secondary">Get In Touch</a>
				</div>
				<div class="hero-animation">
					<div class="floating-box"></div>
				</div>
			</div>
		</section>

		<!-- About Section -->
		<section id="about" class="about">
			<div class="container">
				<h2 class="section-title">About Me</h2>
				<div class="about-content">
					<div class="about-text">
						<p>
							I'm a web developer passionate about creating clean, user-friendly
							digital experiences. With a strong foundation in frontend and
							backend technologies, I focus on building practical solutions that
							solve real problems.
						</p>
						<p>
							I believe in writing maintainable code, thoughtful design, and
							continuous learning. Whether building a website or debugging
							complex issues, I approach every project with attention to detail
							and professionalism.
						</p>
						<div class="about-info">
							<div class="info-item">
								<i class="fas fa-lightbulb"></i>
								<h3>Problem Solving</h3>
							</div>
							<div class="info-item">
								<i class="fas fa-palette"></i>
								<h3>Design</h3>
							</div>
							<div class="info-item">
								<i class="fas fa-code"></i>
								<h3>Development</h3>
							</div>
						</div>
					</div>
				</div>
			</div>
		</section>

		<!-- Skills Section -->
		<section id="skills" class="skills">
			<div class="container">
				<h2 class="section-title">Skills</h2>
				<div class="skills-grid">
					<div class="skill-card">
						<h3>Frontend</h3>
						<ul>
							<li>HTML & CSS</li>
							<li>JavaScript</li>
							<li>React</li>
							<li>Responsive Design</li>
						</ul>
					</div>
					<div class="skill-card">
						<h3>Backend</h3>
						<ul>
							<li>Node.js</li>
							<li>Database Design</li>
							<li>REST APIs</li>
							<li>Server Architecture</li>
						</ul>
					</div>
					<div class="skill-card">
						<h3>Tools</h3>
						<ul>
							<li>Git & GitHub</li>
							<li>VS Code</li>
							<li>npm & webpack</li>
							<li>DevTools</li>
						</ul>
					</div>
					<div class="skill-card">
						<h3>Other</h3>
						<ul>
							<li>Problem Solving</li>
							<li>Team Collaboration</li>
							<li>Communication</li>
							<li>Time Management</li>
						</ul>
					</div>
				</div>
			</div>
		</section>

		<!-- Projects Section -->
		<section id="projects" class="projects">
			<div class="container">
				<h2 class="section-title">Featured Projects</h2>
				<div class="projects-grid">
					<div class="project-card">
						<div class="project-image">
							<div class="placeholder-image">Project 1</div>
						</div>
						<div class="project-info">
							<h3>FADEFREE</h3>
							<p>
								A fully functional e-commerce platform with product listings,
								shopping cart, and checkout functionality.
							</p>
							<div class="project-tech">
								<span class="tech-tag">HTML</span>
								<span class="tech-tag">CSS</span>
								<span class="tech-tag">JavaScript</span>
							</div>
							<div class="project-links">
								<a
									href="https://jeanalen-portfolio.free.nf/?i=1"
									class="project-link"
									title="Visit Website"
								>
									<i class="fas fa-globe"></i>
								</a>
								<a
									href="https://jeanalen.github.io/fadefree/"
									class="project-link"
									title="View Code"
								>
									<i class="fas fa-code"></i>
								</a>
							</div>
						</div>
					</div>

					<div class="project-card">
						<div class="project-image">
							<div class="placeholder-image">Project 2</div>
						</div>
						<div class="project-info">
							<h3>University of Bohol - Stakeholder</h3>
							<p>STAKEHOLDER MEETING ATTENDANCE</p>
							<div class="project-tech">
								<span class="tech-tag">HTML</span>
								<span class="tech-tag">CSS</span>
								<span class="tech-tag">JavaScript</span>
							</div>
							<div class="project-links">
								<a
									href="https://jeanalen.github.io/stakeholders/"
									class="project-link"
									title="Visit Website"
								>
									<i class="fas fa-globe"></i>
								</a>
								<a
									href="https://jeanalen.github.io/stakeholders/"
									class="project-link"
									title="View Code"
								>
									<i class="fas fa-code"></i>
								</a>
							</div>
						</div>
					</div>

					<div class="project-card">
						<div class="project-image">
							<div class="placeholder-image">Project 3</div>
						</div>
						<div class="project-info">
							<h3>Rock Paper Scissors (Python)</h3>
							<p>
								A Python-powered game deployed as a serverless function on
								Vercel.
							</p>
							<div class="project-tech">
								<span class="tech-tag">Python</span>
								<span class="tech-tag">Flask</span>
								<span class="tech-tag">Vercel</span>
							</div>
							<div class="project-links">
								<a
									href="https://https://game-rps-sable.vercel.app"
									class="project-link"
									target="_blank"
									title="Visit Website"
								>
									<i class="fas fa-globe"></i>
								</a>
								<a
									href="https://github.com/jeanalen/game-rps-sable"
									class="project-link"
									target="_blank"
									title="View Code"
								>
									<i class="fas fa-code"></i>
								</a>
							</div>
						</div>
					</div>
				</div>
			</div>
		</section>

		<!-- Contact Section -->
		<section id="contact" class="contact">
			<div class="container">
				<h2 class="section-title">Get In Touch</h2>
				<p class="contact-subtitle">
					Have a question or want to work together? Feel free to reach out.
				</p>

				<div class="contact-content">
					<div class="contact-info">
						<div class="contact-item">
							<i class="fas fa-envelope"></i>
							<div>
								<h3>Email</h3>
								<p>
									<a href="mailto:jeanalen@example.com">jeanalen@example.com</a>
								</p>
							</div>
						</div>
						<div class="contact-item">
							<i class="fas fa-phone"></i>
							<div>
								<h3>Phone</h3>
								<p><a href="tel:+1234567890">+1 (234) 567-890</a></p>
							</div>
						</div>
						<div class="contact-item">
							<i class="fas fa-map-marker-alt"></i>
							<div>
								<h3>Location</h3>
								<p>Your City, Your Country</p>
							</div>
						</div>
					</div>

					<form class="contact-form" id="contactForm">
						<input type="text" placeholder="Your Name" required />
						<input type="email" placeholder="Your Email" required />
						<textarea placeholder="Your Message" rows="5" required></textarea>
						<button type="submit" class="btn btn-primary">Send Message</button>
					</form>
				</div>

				<div class="social-links">
					<a href="#" title="LinkedIn"><i class="fab fa-linkedin"></i></a>
					<a href="#" title="GitHub"><i class="fab fa-github"></i></a>
					<a href="#" title="Twitter"><i class="fab fa-twitter"></i></a>
					<a href="#" title="Instagram"><i class="fab fa-instagram"></i></a>
				</div>
			</div>
		</section>

		<!-- Footer -->
		<footer class="footer">
			<div class="container">
				<p>&copy; 2024 Jeanalen Tabaranza. All rights reserved.</p>
			</div>
		</footer>

		<script src="script.js"></script>
	</body>
</html>
