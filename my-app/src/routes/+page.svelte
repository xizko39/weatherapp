<script lang="ts">
	import type { PageData } from './$types';
	import { onMount } from 'svelte';
  
	export let data: PageData;
	console.log(data);
  
	const locations = ['London', 'New York', 'Paris'];
	let selectedLocation = 'London';
  
	async function fetchData(location: string) {
	  try {
		const res = await fetch(`http://localhost:5000/weather/${location}`);
		const weatherData = await res.json();
		data.weatherforecast = weatherData;
	  } catch (error) {
		console.error('Error fetching weather data:', error);
	  }
	}
  
	function changeLocation(event: Event) {
	  const target = event.target as HTMLSelectElement;
	  selectedLocation = target.value;
	  fetchData(selectedLocation);
	}
  
	function getEmoji(condition: string): string {
	  switch (condition.toLowerCase()) {
		case 'clear':
		  return '☀️'; 
		case 'clouds':
		  return '☁️'; 
		case 'rain':
		  return '🌧️'; 
      case 'drizzle':
		  return '🌧️'; 
		default:
		  return '';
	  }
	}
  
	onMount(() => {
	  fetchData(selectedLocation);
	});
  </script>
  
  <section>
	<div>
		<h3>{data.weatherforecast.location}</h3>
	    <h1>{data.weatherforecast.temperature} °C</h1>
	    <h4>{data.weatherforecast.condition} {getEmoji(data.weatherforecast.condition)}</h4>
	</div>
    
	<div class="dropdown">
	  <select bind:value={selectedLocation} on:change={changeLocation}>
		{#each locations as location}
		  <option value={location}>{location}</option>
		{/each}
	  </select>
	</div>
  </section>
  
<style>
    :global(body) {
        margin: 0;
        padding: 0;
        font-family: 'Arial', sans-serif;
        background: linear-gradient(to bottom, #6495ED, #4169E1);
        background-size: cover;
        transition: background-image 0.5s ease-in-out;
    }

    section {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 100vh;
        text-align: center;
		background-color: rgba(255, 255, 255, 0.2);
    }

    h1 {
        font-size: 5rem;
        margin-bottom: 1rem;
        color: #fff;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    }
	h3 {

        font-size: 4rem;
        margin-bottom: 1rem;
        color: #fff;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);

    }
	h4 {

		font-size: 3rem;
        margin-bottom: 1rem;
        color: #fff;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        margin-bottom: 2rem;
	}


 

    .dropdown {
        position: relative;
        width: 350px;
    }

    .dropdown select {
        appearance: none;
        width: 100%;
        padding: 15px;
        font-size: 1.8rem;
        border: none;
        border-radius: 10px;
        outline: none;
        background-color: rgba(255, 255, 255, 0.2);
        color: #fff;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    .dropdown select:hover {
        background-color: rgba(255, 255, 255, 0.3);
    }

    .dropdown select:focus {
        background-color: rgba(255, 255, 255, 0.4);
		color: black;
    }

    .dropdown::after {
        content: '\25BC';
        position: absolute;
        top: 50%;
        right: 20px;
        transform: translateY(-50%);
        pointer-events: none;
    }
</style>

