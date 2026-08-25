# EventRug — Weave Your Experiences

EventRug is an end-to-end EventTech and social experience platform designed to bridge the gap between digital booking and physical event execution. Rather than ending at the point of ticket sale, EventRug connects the entire event lifecycle into a unified ecosystem for **Attendees**, **Organizers**, **Event Staff**, and **Platform Administrators**.

---

## Key Features

### 1. Customer Experience

* **Discovery & Booking:** Multi-parameter search, dynamic venue exploration, section/seat reservation, and multi-tier ticketing (Daily, Multi-Day, and Session passes).
* **Smart Navigation:** Real-time gate routing, venue entry instructions, and in-venue POI mapping (seats, stages, facilities).
* **Social Community:** Event-specific feeds, media sharing, discussions, and a **Verified Attendee** badge granted exclusively via valid check-in.

### 2. Organizer Portal

* **Digital Venue Builder:** Dynamic section mapping, capacity threshold management, and gate assignments.
* **Operations & Ticketing:** Multi-session pricing, promotional tools, revenue monitoring, and real-time attendance dashboards.
* **Staff Management:** Role-based access control (RBAC) to delegate scanning and wristband linking without exposing financial data.

### 3. Event Staff Operations

* **High-Speed Check-In:** Camera-based QR ticket scanning with instant status validation (duplicate, refunded, wrong session).
* **Physical Credential Mapping:** Associate physical wristbands with digital ticket IDs on-site.

### 4. Administrator Platform

* **Governance & Trust:** Organizer identity verification, venue authorization checks, and event approval workflows.
* **Safety & Finance:** Fraud detection algorithms, dispute resolution, refund handling, and commission payouts.

---

## Tech Stack

* **Mobile App:** React Native CLI, NativeWind (TailwindCSS), Zustand (State Management)
* **Backend API:** Node.js, Express.js, TypeScript
* **Database & Caching:** PostgreSQL, Redis (Seat-locking, background queues, rate limiting)
* **Authentication:** JWT, Role-Based Access Control (RBAC)

---

## System Architecture

```text
       ┌────────────────────────────────────────────────────────┐
       │                  EventRug Platform                     │
       └────────────────────────────────────────────────────────┘
                                   │
      ┌────────────────┬───────────┴────────────┬───────────────┐
      ▼                ▼                        ▼               ▼
┌───────────┐    ┌───────────┐            ┌───────────┐   ┌───────────┐
│ Customer  │    │ Organizer │            │   Staff   │   │   Admin   │
│  Mobile   │    │ Dashboard │            │  Mobile   │   │  Portal   │
└─────┬─────┘    └─────┬─────┘            └─────┬─────┘   └─────┬─────┘
      │                │                        │               │
      └────────────────┼────────────────────────┴───────────────┘
                       ▼
         ┌───────────────────────────┐
         │     Express / Node API    │
         └─────────────┬─────────────┘
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
     ┌───────────────┐   ┌───────────────┐
     │  PostgreSQL   │   │  Redis Cache  │
     │ (Core State)  │   │ (Locks/Queues)│
     └───────────────┘   └───────────────┘

```

---

## Getting Started

### Prerequisites

* Node.js (v18+ recommended)
* PostgreSQL
* Redis
* React Native CLI & Android Studio / Xcode

### Backend Setup

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/EventRug.git
cd EventRug/backend

```


2. **Install dependencies:**
```bash
npm install

```


3. **Configure environment variables:**
Create a `.env` file in the `backend/` root:
```env
PORT=5000
DATABASE_URL=postgresql://user:password@localhost:5432/EventRug_db
REDIS_URL=redis://localhost:6379
JWT_SECRET=your_super_secret_jwt_key

```


4. **Run migrations and start the server:**
```bash
npm run db:migrate
npm run dev

```



### Mobile App Setup

1. **Navigate to the mobile directory:**
```bash
cd ../mobile

```


2. **Install dependencies:**
```bash
npm install

```


3. **Run the application:**
* **Android:**
```bash
npx react-native run-android

```


* **iOS:**
```bash
cd ios && pod install && cd ..
npx react-native run-ios

```





---

## Project Structure

```text
EventRug/
├── backend/
│   ├── src/
│   │   ├── controllers/      # Route controllers
│   │   ├── middlewares/      # Auth & role validations
│   │   ├── models/           # Database models & schemas
│   │   ├── routes/           # REST API endpoints
│   │   ├── services/         # Business logic (Seat locks, QR, payouts)
│   │   └── index.ts          # Server entry point
│   ├── package.json
│   └── tsconfig.json
│
├── mobile/
│   ├── src/
│   │   ├── components/       # Reusable UI components
│   │   ├── navigation/       # React Navigation stacks & tabs
│   │   ├── screens/          # App screens (Discovery, VenueMap, Ticket)
│   │   ├── store/            # Zustand stores
│   │   └── utils/            # Helpers and API client
│   ├── package.json
│   └── App.tsx
│
└── README.md

```

---

