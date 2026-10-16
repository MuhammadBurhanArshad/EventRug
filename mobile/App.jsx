/**
 * EventRug Mobile App
 *
 * @format
 */

import './global.css';
import React from 'react';
import { StatusBar, Text, View, useColorScheme, TouchableOpacity } from 'react-native';
import {
  SafeAreaProvider,
  useSafeAreaInsets,
} from 'react-native-safe-area-context';
import { useEventStore } from './src/store/useEventStore';

function App() {
  const isDarkMode = useColorScheme() === 'dark';

  return (
    <SafeAreaProvider>
      <StatusBar barStyle={isDarkMode ? 'light-content' : 'dark-content'} />
      <AppContent />
    </SafeAreaProvider>
  );
}

function AppContent() {
  const insets = useSafeAreaInsets();
  const { events, setEvents } = useEventStore();

  const handleAddSampleEvent = () => {
    const newEvent = {
      id: `evt-${Date.now()}`,
      title: 'Neon Horizon Music Fest',
      venue: 'Beacon Arena',
    };
    setEvents([...events, newEvent]);
  };

  return (
    <View
      className="flex-1 bg-slate-900 justify-center items-center px-6"
      style={{ paddingTop: insets.top, paddingBottom: insets.bottom }}
    >
      <View className="w-full max-w-md bg-slate-800/80 rounded-2xl p-6 border border-slate-700 items-center">
        <Text className="text-3xl font-extrabold text-indigo-400 tracking-tight mb-2">
          EventRug
        </Text>
        <Text className="text-sm text-slate-400 text-center mb-6">
          NativeWind (Tailwind CSS) & Zustand State Management Ready
        </Text>

        <TouchableOpacity
          activeOpacity={0.8}
          onPress={handleAddSampleEvent}
          className="bg-indigo-600 active:bg-indigo-700 px-5 py-3 rounded-xl mb-4 w-full items-center"
        >
          <Text className="text-white font-semibold text-base">
            Add Sample Event ({events.length})
          </Text>
        </TouchableOpacity>

        {events.length > 0 && (
          <View className="w-full mt-2 space-y-2">
            {events.slice(-3).map((item) => (
              <View key={item.id} className="bg-slate-700/50 p-3 rounded-lg border border-slate-600">
                <Text className="text-white font-medium text-sm">{item.title}</Text>
                <Text className="text-slate-400 text-xs">{item.venue}</Text>
              </View>
            ))}
          </View>
        )}
      </View>
    </View>
  );
}

export default App;
