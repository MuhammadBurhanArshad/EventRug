const BaseRepository = require('./baseRepository');

class EventRepository extends BaseRepository {
  constructor() {
    // Seed sample initial events
    super([
      {
        id: 'event-001',
        title: 'Sonic Loom Music Festival',
        description: 'Multi-stage electronic and indie music experience with interactive light installations.',
        venue: 'Beacon Waterfront Arena, Gate 4',
        category: 'Concert',
        organizerId: 'org-101',
        date: '2026-11-20T18:00:00Z',
        price: 85.0,
        totalCapacity: 500,
        availableCapacity: 450,
        status: 'published',
      },
      {
        id: 'event-002',
        title: 'Apex Gaming & Tech Summit',
        description: 'Keynotes, hardware showcases, esports tournaments, and networking for digital creators.',
        venue: 'Grand Horizon Convention Center, Hall B',
        category: 'Conference',
        organizerId: 'org-102',
        date: '2026-12-05T09:00:00Z',
        price: 150.0,
        totalCapacity: 800,
        availableCapacity: 620,
        status: 'published',
      },
    ]);
  }

  async findByCategory(category) {
    return this.items.filter(
      (event) => event.category.toLowerCase() === category.toLowerCase()
    );
  }

  async findByOrganizer(organizerId) {
    return this.items.filter((event) => event.organizerId === organizerId);
  }

  async decrementCapacity(eventId, count = 1) {
    const event = await this.findById(eventId);
    if (!event) return null;
    if (event.availableCapacity < count) return false;

    return this.update(eventId, {
      availableCapacity: event.availableCapacity - count,
    });
  }
}

module.exports = new EventRepository();
