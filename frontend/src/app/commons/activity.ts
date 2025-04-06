export interface Activity {
    name: string;
    description: string;
    address: string | null;
    type: 'EVENT' | 'TOURISTIC_ATTRACTION';
    date: string | null;
    time: string | null;
    source: string | null;
}