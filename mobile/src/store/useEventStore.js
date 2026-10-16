import { create } from 'zustand';

export const useEventStore = create((set) => ({
  events: [],
  selectedEvent: null,
  isLoading: false,
  error: null,

  setEvents: (events) => set({ events }),
  selectEvent: (event) => set({ selectedEvent: event }),
  setLoading: (isLoading) => set({ isLoading }),
  setError: (error) => set({ error }),
}));
