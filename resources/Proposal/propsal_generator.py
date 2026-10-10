import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

doc = Document()

# Base Page Margins (Standard Academic 1-inch)
for s in doc.sections:
    s.top_margin = Inches(1.0)
    s.bottom_margin = Inches(1.0)
    s.left_margin = Inches(1.0)
    s.right_margin = Inches(1.0)

NAVY = RGBColor(11, 44, 91)
SLATE = RGBColor(50, 50, 50)
WHITE = RGBColor(255, 255, 255)

def set_cell_background(cell, fill_hex):
    tcPr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=140, right=140):
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}>'
                      f'<w:top w:w="{top}" w:type="dxa"/>'
                      f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
                      f'<w:left w:w="{left}" w:type="dxa"/>'
                      f'<w:right w:w="{right}" w:type="dxa"/>'
                      f'</w:tcMar>')
    tcPr.append(tcMar)

def set_table_center(table):
    tblPr = table._element.xpath('w:tblPr')
    if tblPr:
        jc = parse_xml(f'<w:jc {nsdecls("w")} w:val="center"/>')
        tblPr[0].append(jc)

def add_heading_1(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(16)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    r.font.name = "Arial"
    r.font.size = Pt(13)
    r.font.bold = True
    r.font.color.rgb = NAVY

def add_body_p(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.line_spacing = 1.15
    r = p.add_run(text)
    r.font.name = "Arial"
    r.font.size = Pt(10)
    r.font.color.rgb = SLATE
    return p

def add_bullet_item(bold_prefix, text):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_bold = p.add_run(bold_prefix + " ")
        r_bold.font.name = "Arial"
        r_bold.font.size = Pt(10)
        r_bold.font.bold = True
        r_bold.font.color.rgb = NAVY
    r_text = p.add_run(text)
    r_text.font.name = "Arial"
    r_text.font.size = Pt(10)
    r_text.font.color.rgb = SLATE

# ==================== COVER PAGE ====================
p_title = doc.add_paragraph()
p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_title.paragraph_format.space_before = Pt(40)
r_title = p_title.add_run("SocioRug\nProject Proposal")
r_title.font.name = "Arial"
r_title.font.size = Pt(26)
r_title.font.bold = True
r_title.font.color.rgb = NAVY

p_sub = doc.add_paragraph()
p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_sub.paragraph_format.space_after = Pt(28)
r_sub = p_sub.add_run("A Complete Event Discovery, Management, Venue, Ticketing,\nNavigation, Attendance & Social Experience Platform")
r_sub.font.name = "Arial"
r_sub.font.size = Pt(12)
r_sub.font.italic = True
r_sub.font.color.rgb = RGBColor(90, 90, 90)

p_meta = doc.add_paragraph()
p_meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_meta.paragraph_format.line_spacing = 1.25

def add_meta(label, val):
    r1 = p_meta.add_run(f"{label}\n")
    r1.font.name = "Arial"
    r1.font.size = Pt(11)
    r1.font.bold = True
    r1.font.color.rgb = NAVY
    r2 = p_meta.add_run(f"{val}\n\n")
    r2.font.name = "Arial"
    r2.font.size = Pt(10.5)
    r2.font.color.rgb = SLATE

add_meta("Supervisor", "Adil Ahmed Unar")
add_meta("Submitted by", "Burhan  { Registration ID }\nBasil  { Registration ID }")
add_meta("Faculty & Institution", "Faculty of Computing and Engineering Sciences\nShaheed Zulfiqar Ali Bhutto Institute of Science and Technology, Karachi.")
add_meta("Date", "[ September - 2026 ]")

doc.add_page_break()

# ==================== 1. INTRODUCTION ====================
add_heading_1("1. Introduction")
add_body_p("Modern event technology remains heavily fragmented, operating as isolated systems for event discovery, ticketing, physical access control, venue navigation, and community interaction[cite: 5]. Traditional event platforms disengage immediately after issuing a digital ticket or static QR code, leaving attendees unassisted as they physically arrive, locate venue gates, find assigned seats, and navigate complex event spaces[cite: 5].")
add_body_p("SocioRug is envisioned as a next-generation EventTech platform designed to bring the entire event lifecycle into one connected digital ecosystem[cite: 5]. Connecting Event Organizers, Customers/Attendees, Event Staff, Venues, and Platform Administrators through a single application, SocioRug goes significantly beyond conventional ticketing services[cite: 5]. A customer does not simply discover an event, buy a ticket, and receive a QR code; rather, the platform accompanies them through every step of their journey: Discover → Explore → Select → Book → Pay → Navigate → Arrive → Check In → Access → Experience → Share → Connect[cite: 5]. By ensuring that the digital experience continues seamlessly throughout the physical event, SocioRug provides a cohesive operating environment for modern live events[cite: 5].")

# ==================== 2. OBJECTIVE ====================
add_heading_1("2. Objective")
add_body_p("The primary objective of SocioRug is to transform traditional, disconnected ticketing platforms into a fully unified digital operating ecosystem that bridges digital purchases with on-ground venue operations[cite: 5]. The platform aims to:")
add_bullet_item("Unify the Event Lifecycle:", "Eliminate operational fragmentation by connecting discovery, interactive venue selection, payments, gate routing, check-in, and post-event reviews[cite: 5].")
add_bullet_item("Interactive Digital Venue Mapping:", "Allow organizers to construct multi-tier digital venues (stages, gates, sections, seats, facilities) and provide customers with transparent, real-time visual seat selection[cite: 5].")
add_bullet_item("Streamline Gate & Entrance Operations:", "Provide on-ground event staff with high-throughput QR validation and physical wristband association to eradicate entrance bottlenecks and counterfeit tickets[cite: 5].")
add_bullet_item("Provide Turn-by-Turn Navigation:", "Deliver intelligent navigation to direct attendees to designated parking zones, specific exterior gates, and interior points of interest[cite: 5].")
add_bullet_item("Cultivate Verified Event Communities:", "Foster an event-centric social feed and dual-tier review framework that prioritizes feedback and media from verified attendees[cite: 5].")
add_bullet_item("Enable Comprehensive Administration:", "Equip organizers and platform administrators with end-to-end financial settlement tools, flexible session pricing models, KYC verification workflows, and crowd traffic analytics[cite: 5].")

# ==================== 3. PROBLEM DESCRIPTION ====================
add_heading_1("3. Problem Description")
add_body_p("Problem: In the live events industry, organizers and attendees face severe inefficiencies resulting from fragmented tools[cite: 5]. Traditional ticketing portals function merely as transactional checkouts; once a customer purchases a ticket, the digital connection ends[cite: 5]. Customers arrive at massive venues without clear guidance on which exterior gate to enter, causing long queues and dangerous crowding at main gates while secondary entrances sit idle[cite: 5]. Inside venues, attendees struggle to locate their assigned seats, amenities, restrooms, and emergency exits[cite: 5]. For organizers, managing physical access control through separate third-party ticketing, manual guest lists, and detached wristband distribution invites fraud, unauthorized ticket duplication, and operational chaos[cite: 5]. Furthermore, post-event engagement is scattered across unverified social platforms, making community building and feedback unreliable[cite: 5].")
add_body_p("Solution: SocioRug resolves these challenges by maintaining a continuous digital connection throughout the physical event[cite: 5]. By synchronizing digital venue maps with real-time seat inventory, directing attendees to specific exterior gates via GPS routing, enabling event staff to pair physical wristbands directly with scanned QR tickets, providing interactive in-venue wayfinding, and restricting social review badges to verified check-ins, SocioRug delivers an integrated, fraud-resistant operating system for events of any scale[cite: 5].")

# ==================== 4. TARGET INDUSTRY & AUDIENCE ====================
add_heading_1("4. Target Industry & Audience")
add_body_p("Target Industry: SocioRug is designed for the Live Entertainment, Conference, and Venue Operations Industry, specifically targeting[cite: 5]:")
add_bullet_item("Music Festivals & Concert Promoters:", "Organizations requiring complex multi-gate crowd routing, general admission/VIP zoning, and rapid physical wristband credentialing[cite: 5].")
add_bullet_item("Sports Stadiums & Arenas:", "Large-scale venues needing granular section/row/seat selection, concourse crowd management, and emergency wayfinding[cite: 5].")
add_bullet_item("Academic & Professional Conferences:", "Universities, research symposiums, and corporate exhibitions needing multi-day passes, session-specific room pricing, and verified attendee networking[cite: 5].")
add_body_p("Target Audience: The platform directly serves four key user personas[cite: 5]:")
add_bullet_item("Attendees / Customers:", "Individuals seeking transparent event discovery, interactive seat booking, directional gate guidance, and verified social engagement[cite: 5].")
add_bullet_item("Event Organizers:", "Event managers needing complete control over venue mapping, multi-day ticket tiers, staff permissions, and real-time revenue analytics[cite: 5].")
add_bullet_item("Event Staff:", "On-ground gate attendants, ushers, and security teams executing rapid QR scanning, wristband linking, and attendee assistance[cite: 5].")
add_bullet_item("Platform Administrators:", "System supervisors managing organizer KYC compliance, event legitimacy approvals, financial reconciliations, and platform security[cite: 5].")

# ==================== 5. METHODOLOGY ====================
add_heading_1("5. Methodology")
add_body_p("The project will follow an Agile Development Methodology with bi-weekly iterative sprints and continuous integration, ensuring steady progress, modular development, and adaptability[cite: 3, 4]:")
add_bullet_item("1. Requirement Analysis & Planning:", "Define detailed SRS and SDS documents, architect the relational database schema, design API endpoint specifications, and construct UI/UX wireframes[cite: 1, 2, 3, 4].")
add_bullet_item("2. Frontend Development (Web & Mobile):", "Build responsive web portals for Attendees, Organizers, and Admins using React.js and Tailwind CSS; build high-performance mobile scanning and navigation interfaces using React Native[cite: 3, 4, 5].")
add_bullet_item("3. Backend & API Engineering:", "Implement a scalable RESTful architecture using Node.js and Express.js, manage database operations via Prisma ORM with PostgreSQL, and enforce role-based access control (RBAC) via JWT[cite: 3, 5].")
add_bullet_item("4. Concurrency & High-Availability Logic:", "Integrate Redis caching to support distributed seat reservation locks, avoiding double bookings during high-traffic ticketing windows[cite: 5].")
add_bullet_item("5. Field Testing & Quality Assurance:", "Conduct automated unit testing, end-to-end integration testing, offline scanner verification, and load testing simulating simultaneous ticket checkouts[cite: 1, 2, 3, 4].")
add_bullet_item("6. Deployment & Maintenance:", "Deploy containerized services using Docker to scalable cloud infrastructure, establishing continuous monitoring, backup procedures, and audit logging[cite: 3].")

# ==================== 6. PROJECT SCOPE & DETAILED FEATURES LIST ====================
add_heading_1("6. Project Scope & Detailed Features List")
add_body_p("SocioRug unifies discovery, venue design, ticketing, operations, and social networking. The system consists of 14 core features[cite: 5]:")

features_list = [
    ("Feature 1: User Authentication & Role-Based Access Control (RBAC)",
     "Provides secure, isolated authentication for Attendees, Organizers, Event Staff, and Admins. Features include JWT-based token generation, encrypted password handling, phone/email OTP verification, session expiration, and granular permission enforcement preventing operational staff from accessing financial or administrative data[cite: 3, 5]."),
    ("Feature 2: Organizer Registration & KYC Verification Workflow",
     "Enforces trust and legitimacy before an organizer can host public events. Organizers must submit legal identity documentation, company credentials, and venue authorization contracts. Platform Administrators review, approve, reject, or request additional data through a dedicated verification pipeline[cite: 5]."),
    ("Feature 3: Interactive Digital Venue Mapping & Builder",
     "A visual CAD-lite layout builder enabling organizers to construct complete digital twins of physical venues. Supports configuring stages, VIP lounges, general admission zones, seated sections, rows, individual seats, entrance gates, emergency exits, parking zones, restrooms, and first-aid stations[cite: 5]."),
    ("Feature 4: Dynamic Seating Inventory & Concurrency Reservation",
     "Enables real-time seat status visualization (Available, Reserved, Sold Out). Utilizes distributed memory locking via Redis with 10-minute countdown timers, temporarily reserving selected seats during checkout to strictly prevent race conditions and double bookings[cite: 5]."),
    ("Feature 5: Multi-Day, Session-Based & Flexible Ticketing Engine",
     "Accommodates diverse event formats including single-day tickets, multi-day passes, daily recurring passes, individual room sessions, and early-bird promotional codes. Generates unique, dynamically signed QR tickets linked to specific dates and access tiers[cite: 5]."),
    ("Feature 6: Payment Processing & Financial Split Settlement",
     "Facilitates secure online checkout via credit/debit cards and digital mobile wallets. Features automated financial ledgering that splits gross transactions into payment gateway processing fees, SocioRug platform commission, and organizer net revenue, providing automated invoicing and refund tracking[cite: 3, 5]."),
    ("Feature 7: Exterior Gate Navigation & Crowd Routing",
     "Directs attendees to their specific entry point rather than a generic venue address. Maps ticket tiers directly to exterior gates (e.g., General Admission to Gate 3, VIP to Gate 1) and provides driving, parking, and walking directions to minimize entrance bottlenecks[cite: 5]."),
    ("Feature 8: High-Throughput QR Validation & Check-in",
     "A camera scanner utility tailored for on-ground staff mobile devices. Delivers sub-second cryptographic QR verification, instantly detecting and flagging duplicate scans, already-used passes, refunded tickets, wrong event tickets, and invalid dates[cite: 5]."),
    ("Feature 9: Physical Wristband Pairing & Credentialing",
     "Bridges digital tickets with physical access credentials. Allows event staff to scan a verified QR code, scan or input an RFID/alphanumeric wristband ID, and create an immutable audit record: Customer + Ticket ID + Wristband ID + Gate Staff ID + Timestamp[cite: 5]."),
    ("Feature 10: In-Venue Wayfinding & Interactive Map",
     "Assists attendees after crossing venue perimeter gates. Provides an interactive vector map showing their location relative to their assigned section, seat number, nearest restrooms, merchandise booths, medical centers, and emergency exits[cite: 5]."),
    ("Feature 11: Verified Attendee Social Stream & Community",
     "Transforms events into dedicated digital communities. Attendees can share photos, updates, and discussions. Users who have completed physical gate check-in receive an exclusive 'Verified Attendee' badge on their posts to eliminate unverified spam[cite: 5]."),
    ("Feature 12: Dual-Tier Reviews & Rating System",
     "Collects feedback across multiple parameters: venue organization, sound/stage quality, security, and amenities. Clearly categorizes submissions into 'Verified Attendee Reviews' and 'General Public Feedback' to protect platform integrity[cite: 5]."),
    ("Feature 13: Push Notifications & Emergency Broadcast Center",
     "Keeps attendees and staff informed via automated alerts for gate assignments, schedule changes, and weather advisories, along with a high-priority emergency broadcast tool to deliver immediate safety notices to all on-site devices[cite: 3, 5]."),
    ("Feature 14: Comprehensive Organizer & Admin Analytics Dashboards",
     "Provides deep business intelligence. Organizers monitor real-time gate traffic velocity, capacity consumption, revenue breakdowns, and check-in rates. Administrators track platform gross transaction value, commission splits, and risk-scored audit logs[cite: 5].")
]

for title, desc in features_list:
    add_bullet_item(title + ":", desc)

# ==================== 7. FEASIBILITY STUDY ====================
add_heading_1("7. Feasibility Study")
add_bullet_item("Technical Feasibility:", "The platform utilizes modern, production-proven technologies. The frontend and administrative portals utilize React.js with Tailwind CSS, while mobile scanning and attendee navigation are built on React Native. The backend RESTful API is implemented in Node.js and Express.js paired with PostgreSQL and Prisma ORM for relational consistency. Redis is integrated to reliably handle high-concurrency seat reservation locks[cite: 3, 4, 5].")
add_bullet_item("Operational Feasibility:", "By dividing the platform into four role-specific interfaces (Attendee, Organizer, Staff, Admin), operational friction is minimized. Event staff require zero technical onboarding; the mobile scanner operates via a one-tap visual feedback interface (Green for Valid, Red for Invalid, Yellow for Attention)[cite: 5].")
add_bullet_item("Risk Assessment & Mitigation (Data Security):", "SocioRug handles identity documents (KYC), transactions, and real-time attendance data. Mitigation includes bcrypt password hashing, stateless JWT authentication, end-to-end TLS/HTTPS encryption, and strict role-based data isolation ensuring staff cannot view sensitive organizer records[cite: 3, 5].")
add_bullet_item("Risk Assessment & Mitigation (Concurrency Locking):", "High-volume ticket releases can create race conditions where two users attempt to purchase the exact same seat simultaneously. Mitigation involves Redis distributed keys with 10-minute Time-To-Live (TTL) expirations and atomic SQL database transactions[cite: 5].")
add_bullet_item("Risk Assessment & Mitigation (Venue Network Outages):", "Cellular networks frequently degrade at crowded venues. Mitigation includes signed cryptographic QR tickets that can be validated locally by staff devices against an offline pre-synced check-in manifest[cite: 5].")

# ==================== 8. SOLUTION APPLICATION AREAS ====================
add_heading_1("8. Solution Application Areas")
add_body_p("SocioRug is designed to be highly adaptable across diverse event domains[cite: 5]:")
add_bullet_item("Live Concerts & Music Festivals:", "Coordinating massive general admission and VIP areas, multi-gate arrival routing, and instant physical wristband pairing[cite: 5].")
add_bullet_item("Sports Arenas & Stadiums:", "Managing multi-tiered seated sections, row-level wayfinding, concourse crowd management, and high-velocity gate check-ins[cite: 5].")
add_bullet_item("Academic & Professional Conferences:", "Facilitating multi-day badges, session-specific room capacities, keynote check-ins, and verified attendee networking[cite: 5].")
add_bullet_item("Exhibitions & Trade Expos:", "Digitizing floor plans, exhibitor booth wayfinding, visitor credentialing, and multi-hall attendee density monitoring[cite: 5].")

# ==================== 9. TOOLS & TECHNOLOGY ====================
add_heading_1("9. Tools & Technology")
add_body_p("The project utilizes a scalable full-stack engineering stack designed for responsiveness and reliability[cite: 3, 4, 5]:")

tools_data = [
    ("Hardware Tools", "Desktop / Laptop Workstations, Android & iOS Mobile Testing Devices[cite: 1, 2, 4]"),
    ("Web Frontend", "React.js, Tailwind CSS, TypeScript, HTML5, Axios[cite: 1, 3, 4]"),
    ("Mobile Applications", "React Native (Customer Discovery/Wayfinding & Staff Scanner)[cite: 5]"),
    ("Backend API Engine", "Node.js, Express.js Framework (RESTful Architecture)[cite: 1, 3, 4, 5]"),
    ("Database & ORM", "PostgreSQL (Relational Storage), Prisma ORM[cite: 3, 5]"),
    ("In-Memory Cache", "Redis (Distributed Seat Reservation Locks & Session Caching)[cite: 5]"),
    ("Mapping & Wayfinding", "Mapbox SDK, Leaflet.js, Interactive SVG/Canvas Engine[cite: 5]"),
    ("Security & Auth", "JSON Web Tokens (JWT), Bcrypt.js, Role-Based Access Control (RBAC)[cite: 3, 5]"),
    ("Testing & DevOps", "Postman (API QA), Git/GitHub (Version Control), Docker Containers[cite: 3, 5]")
]

t_table = doc.add_table(rows=1, cols=2)
set_table_center(t_table)
for c in t_table.rows[0].cells:
    set_cell_background(c, "0B2C5B")
t_table.rows[0].cells[0].text = "Category"
t_table.rows[0].cells[1].text = "Selected Tools & Frameworks"
for c in t_table.rows[0].cells:
    for p in c.paragraphs:
        for r in p.runs:
            r.font.name = "Arial"
            r.font.size = Pt(10)
            r.font.bold = True
            r.font.color.rgb = WHITE

for cat, desc in tools_data:
    row = t_table.add_row()
    row.cells[0].text = cat
    row.cells[1].text = desc
    for c in row.cells:
        set_cell_margins(c, 80, 80, 120, 120)
        for p in c.paragraphs:
            for r in p.runs:
                r.font.name = "Arial"
                r.font.size = Pt(9.5)
                r.font.color.rgb = SLATE

# ==================== 10. EXPERTISE OF THE TEAM MEMBERS ====================
add_heading_1("10. Expertise of the Team Members")
add_bullet_item("Burhan (Full-Stack & Backend Developer):", "Proficient in Node.js, Express.js, TypeScript, PostgreSQL, and Prisma ORM. Experienced with React Native mobile development, RESTful API architecture, and Linux server environments. Responsible for developing backend services, database relational schemas, Redis concurrency seat locks, payment integrations, and the staff mobile scanner application[cite: 5].")
add_bullet_item("Basil (Frontend & UI/UX Developer):", "Proficient in React.js, JavaScript, Tailwind CSS, HTML5, and responsive UI design. Experienced in state management, API integration, and wireframe prototyping. Responsible for engineering the customer web portal, interactive digital venue builder, organizer management dashboard, and admin oversight consoles[cite: 5].")

# ==================== 11. MILESTONES (FYP-I & FYP-II) ====================
add_heading_1("11. Milestones (FYP-I & FYP-II)")
add_body_p("FYP-I Milestones:")
add_bullet_item("Milestone 1 (SRS, SDS & Architecture Documentation - Weeks 1–4):", "Complete requirements specifications, entity-relationship diagrams, API route contracts, and UI/UX wireframes[cite: 1, 2, 3, 4].")
add_bullet_item("Milestone 2 (Authentication, RBAC & Organizer KYC Verification - Weeks 5–7):", "Deploy secure multi-role JWT authentication, organizer document uploads, and Admin approval consoles[cite: 1, 2, 3, 5].")
add_bullet_item("Milestone 3 (Digital Venue Layout Builder & Section Engine - Weeks 8–11):", "Build the interactive canvas venue builder allowing organizers to define sections, rows, gates, and amenities[cite: 5].")
add_bullet_item("Milestone 4 (Event Creation & Multi-Tier Ticketing Engine - Weeks 12–14):", "Deliver event listing tools, multi-day/session pass logic, dynamic inventory generation, and pricing setup[cite: 5].")
add_bullet_item("Milestone 5 (FYP-I Prototype Integration, Testing & Defense - Weeks 15–16):", "Perform end-to-end integration of FYP-I modules, run user testing, and submit the FYP-I report and defense demo[cite: 3].")

add_body_p("FYP-II Milestones:")
add_bullet_item("Milestone 6 (Distributed Seat Locking & Payment Processing - Weeks 17–19):", "Implement Redis distributed reservation locking, payment gateway checkout, automated invoices, and payout ledgers[cite: 3, 5].")
add_bullet_item("Milestone 7 (Staff Access Control, QR Scanning & Wristbands - Weeks 20–22):", "Build the React Native mobile scanner, cryptographic ticket verification, and physical wristband pairing workflow[cite: 5].")
add_bullet_item("Milestone 8 (Exterior Gate Navigation & In-Venue Wayfinding - Weeks 23–25):", "Implement geospatial routing to assigned gates and interactive indoor SVG wayfinding to seats and amenities[cite: 5].")
add_bullet_item("Milestone 9 (Verified Attendee Social Stream & Reviews - Weeks 26–28):", "Deploy event-specific social discussion feeds, verified attendee badges, and multi-criteria review systems[cite: 5].")
add_bullet_item("Milestone 10 (Push Notifications & Business Intelligence Analytics - Weeks 29–30):", "Build emergency broadcast dispatchers, gate traffic telemetry, and administrative platform analytics[cite: 3, 5].")
add_bullet_item("Milestone 11 (Final System QA, Staging Deployment & Final Defense - Weeks 31–32):", "Conduct end-to-end stress testing, mobile optimization, cloud deployment, and submit final FYP-II documentation[cite: 1, 2, 3, 4].")

# ==================== 12. PROJECT SCHEDULE ====================
add_heading_1("12. Project Schedule (Gantt Chart)")
add_body_p("Detailed weekly timeline across the 32-week final year project lifecycle:")

schedule_data = [
    # FYP-I
    ("FYP-I", "Task 1: SRS & SDS Documentation", "W01 - W04", "Requirements, ER diagrams, Wireframes[cite: 1, 2, 3, 4]"),
    ("FYP-I", "Task 2: Database Modeling & API Architecture", "W03 - W05", "PostgreSQL schema, Prisma setup, REST APIs[cite: 3, 5]"),
    ("FYP-I", "Task 3: RBAC & Organizer KYC Portal", "W05 - W07", "JWT auth, KYC document upload, Admin review[cite: 3, 5]"),
    ("FYP-I", "Task 4: Digital Venue Layout Builder", "W08 - W11", "Visual canvas tool, seat/section configuration[cite: 5]"),
    ("FYP-I", "Task 5: Event Publishing & Ticketing Engine", "W12 - W14", "Multi-day/session pass creation, pricing[cite: 5]"),
    ("FYP-I", "Task 6: FYP-I Integration, Report & Mid-Defense", "W15 - W16", "Prototype integration, testing, defense demo[cite: 3]"),
    # FYP-II
    ("FYP-II", "Task 7: Redis Seat Locking & Payment Gateway", "W17 - W19", "Concurrency locks, checkout, split settlement[cite: 3, 5]"),
    ("FYP-II", "Task 8: Staff QR Scanner & Wristband Pairing", "W20 - W22", "Mobile scanner app, RFID/wristband linking[cite: 5]"),
    ("FYP-II", "Task 9: Gate Navigation & In-Venue Wayfinding", "W23 - W25", "Geospatial gate routing, indoor seat maps[cite: 5]"),
    ("FYP-II", "Task 10: Verified Attendee Social & Reviews", "W26 - W28", "Event feed, verified badges, rating engine[cite: 5]"),
    ("FYP-II", "Task 11: Push Alerts, Emergency & Analytics", "W29 - W30", "Broadcast center, gate telemetry, audit logs[cite: 3, 5]"),
    ("FYP-II", "Task 12: Final Integration, QA & FYP-II Defense", "W31 - W32", "Stress testing, cloud deployment, final defense[cite: 1, 2, 3, 4]")
]

sched_tbl = doc.add_table(rows=1, cols=4)
set_table_center(sched_tbl)
for c in sched_tbl.rows[0].cells:
    set_cell_background(c, "0B2C5B")
sched_tbl.rows[0].cells[0].text = "Phase"
sched_tbl.rows[0].cells[1].text = "Task Description"
sched_tbl.rows[0].cells[2].text = "Duration"
sched_tbl.rows[0].cells[3].text = "Deliverables"
for c in sched_tbl.rows[0].cells:
    for p in c.paragraphs:
        for r in p.runs:
            r.font.name = "Arial"
            r.font.size = Pt(10)
            r.font.bold = True
            r.font.color.rgb = WHITE

for phase, desc, dur, deliv in schedule_data:
    row = sched_tbl.add_row()
    row.cells[0].text = phase
    row.cells[1].text = desc
    row.cells[2].text = dur
    row.cells[3].text = deliv
    for c in row.cells:
        set_cell_margins(c, 70, 70, 100, 100)
        for p in c.paragraphs:
            for r in p.runs:
                r.font.name = "Arial"
                r.font.size = Pt(9)
                r.font.color.rgb = SLATE

# ==================== 13. WORK BREAKDOWN STRUCTURE (WBS) ====================
add_heading_1("13. Work Breakdown Structure (WBS)")
add_body_p("Hierarchical decomposition of project phases and engineering deliverables[cite: 1, 2, 3, 4]:")

wbs_data = [
    ("Phase 1 (FYP-I)", "Task 1.1", "System Requirements & Specification Documentation (SRS, SDS, Architecture)[cite: 1, 2, 3, 4]"),
    ("Phase 1 (FYP-I)", "Task 1.2", "Relational Database Schema Design & Prisma ORM Modeling[cite: 3, 5]"),
    ("Phase 1 (FYP-I)", "Task 1.3", "Role-Based Authentication (RBAC) & Organizer KYC Document Verification[cite: 3, 5]"),
    ("Phase 1 (FYP-I)", "Task 1.4", "Interactive Digital Venue Builder (Gates, Stages, Sections, Rows, Seats)[cite: 5]"),
    ("Phase 1 (FYP-I)", "Task 1.5", "Multi-Day, Session-Based Ticketing & Real-Time Seating Engine[cite: 5]"),
    ("Phase 1 (FYP-I)", "Task 1.6", "FYP-I System Integration, Verification Testing & Mid-Term Defense[cite: 3]"),
    ("Phase 2 (FYP-II)", "Task 2.1", "Distributed Redis Concurrency Seat Reservation Locking & Payment Gateway[cite: 3, 5]"),
    ("Phase 2 (FYP-II)", "Task 2.2", "React Native Mobile QR Scanner & Physical Wristband Association Workflow[cite: 5]"),
    ("Phase 2 (FYP-II)", "Task 2.3", "Geospatial Exterior Gate Navigation & In-Venue SVG Wayfinding[cite: 5]"),
    ("Phase 2 (FYP-II)", "Task 2.4", "Verified Attendee Social Streams, Discussions & Multi-Criteria Reviews[cite: 5]"),
    ("Phase 2 (FYP-II)", "Task 2.5", "Emergency Alert Broadcasts, Real-Time Telemetry & Financial Ledgers[cite: 3, 5]"),
    ("Phase 2 (FYP-II)", "Task 2.6", "System Stress Testing, Cloud Deployment, Final Documentation & Defense[cite: 1, 2, 3, 4]")
]

wbs_tbl = doc.add_table(rows=1, cols=3)
set_table_center(wbs_tbl)
for c in wbs_tbl.rows[0].cells:
    set_cell_background(c, "0B2C5B")
wbs_tbl.rows[0].cells[0].text = "Phase"
wbs_tbl.rows[0].cells[1].text = "WBS ID"
wbs_tbl.rows[0].cells[2].text = "Work Package Deliverable"
for c in wbs_tbl.rows[0].cells:
    for p in c.paragraphs:
        for r in p.runs:
            r.font.name = "Arial"
            r.font.size = Pt(10)
            r.font.bold = True
            r.font.color.rgb = WHITE

for ph, wbs_id, desc in wbs_data:
    row = wbs_tbl.add_row()
    row.cells[0].text = ph
    row.cells[1].text = wbs_id
    row.cells[2].text = desc
    for c in row.cells:
        set_cell_margins(c, 70, 70, 100, 100)
        for p in c.paragraphs:
            for r in p.runs:
                r.font.name = "Arial"
                r.font.size = Pt(9)
                r.font.color.rgb = SLATE

# ==================== 14. REFERENCES ====================
add_heading_1("14. References")
refs = [
    ("Eventbrite Developer Platform:", "Building Modern Event Operations, Ticketing Lifecycles, and Webhook Integrations. Eventbrite Architecture Documentation (2024)[cite: 5]."),
    ("Ticketmaster Enterprise Engineering:", "Interactive Digital Seating Configuration and High-Volume Access Control Systems. Ticketmaster Technical Whitepaper (2024)[cite: 5]."),
    ("Mapbox Navigation Architecture:", "Custom Vector Map Rendering, Indoor Point-of-Interest Integration, and Turn-by-Turn Routing. Mapbox Developer Documentation (2024)[cite: 5]."),
    ("PostgreSQL Global Development Group:", "Handling High-Concurrency Transactions, Optimistic Concurrency Control, and Row-Level Locking in Reservation Architectures. PostgreSQL Documentation (2024)[cite: 3]."),
    ("Redis Labs Technical Documentation:", "Implementing Distributed Locks, Atomic Operations, and Key Expirations for Real-Time Inventory Control. Redis Technical Papers (2024)[cite: 5].")
]
for prefix, ref_text in refs:
    add_bullet_item(prefix, ref_text)

doc.save("SocioRug_FYP_Proposal.docx")
print("Saved complete proposal to SocioRug_FYP_Proposal.docx")