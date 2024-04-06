<!-- src/components/MedicationList.svelte -->

<script>
  import { onMount } from 'svelte';
  let medications = [];

  onMount(async () => {
    const response = await fetch('http://localhost:5000/medications');
    medications = await response.json();
  });
</script>

<h2>Medication List</h2>

<ul>
  {#each medications as medication}
    <li>{medication.name} - Quantity: {medication.quantity}</li>
  {/each}
</ul>
