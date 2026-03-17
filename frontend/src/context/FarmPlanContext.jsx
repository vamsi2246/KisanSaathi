import React, { createContext, useContext, useState, useCallback } from 'react';

const STORAGE_KEY = 'kisansaathi_farm_plan';

function load() {
    try {
        const raw = localStorage.getItem(STORAGE_KEY);
        return raw ? JSON.parse(raw) : null;
    } catch {
        return null;
    }
}

function save(data) {
    try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
    } catch {
        // storage quota exceeded
    }
}

const FarmPlanContext = createContext(null);

export function FarmPlanProvider({ children }) {
    const [state, setState] = useState(() => load() ?? { result: null, formData: null });

    const setFarmPlan = useCallback((result, formData) => {
        const next = { result, formData };
        setState(next);
        save(next);
    }, []);

    const clearFarmPlan = useCallback(() => {
        setState({ result: null, formData: null });
        localStorage.removeItem(STORAGE_KEY);
    }, []);

    return (
        <FarmPlanContext.Provider value={{ ...state, setFarmPlan, clearFarmPlan }}>
            {children}
        </FarmPlanContext.Provider>
    );
}

export function useFarmPlan() {
    const ctx = useContext(FarmPlanContext);
    if (!ctx) throw new Error('useFarmPlan must be used inside <FarmPlanProvider>');
    return ctx;
}
