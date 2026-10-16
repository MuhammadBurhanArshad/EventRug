/**
 * Abstract BaseRepository defining CRUD access layer.
 * Can be backed by In-Memory data, PostgreSQL pool, Prisma, or Sequelize.
 */
class BaseRepository {
  constructor(initialData = []) {
    this.items = [...initialData];
  }

  async findAll(filter = {}) {
    let result = [...this.items];
    for (const [key, value] of Object.entries(filter)) {
      if (value !== undefined) {
        result = result.filter((item) => String(item[key]).toLowerCase() === String(value).toLowerCase());
      }
    }
    return result;
  }

  async findById(id) {
    const item = this.items.find((i) => String(i.id) === String(id));
    return item ? { ...item } : null;
  }

  async findOne(predicate) {
    const item = this.items.find(predicate);
    return item ? { ...item } : null;
  }

  async create(data) {
    const newItem = {
      id: data.id || `id_${Date.now()}_${Math.random().toString(36).substring(2, 7)}`,
      ...data,
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString(),
    };
    this.items.push(newItem);
    return { ...newItem };
  }

  async update(id, updates) {
    const index = this.items.findIndex((i) => String(i.id) === String(id));
    if (index === -1) return null;

    this.items[index] = {
      ...this.items[index],
      ...updates,
      updatedAt: new Date().toISOString(),
    };
    return { ...this.items[index] };
  }

  async delete(id) {
    const index = this.items.findIndex((i) => String(i.id) === String(id));
    if (index === -1) return false;

    this.items.splice(index, 1);
    return true;
  }

  async count(filter = {}) {
    const items = await this.findAll(filter);
    return items.length;
  }
}

module.exports = BaseRepository;
