
export const load = async ({fetch}: {fetch: any}) => {
    const weatherres = await fetch('http://localhost:5000/weather/london');
    const weatherdata = await weatherres.json();
    const weather = weatherdata;
    return {
        weatherforecast: weather
    };
};
