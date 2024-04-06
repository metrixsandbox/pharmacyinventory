<!-- src/components/MedicationList.svelte -->
<script>
    // Define medication data
    let medications = [
      { id: 1, name: "Medication A", quantity: 10 },
      { id: 2, name: "Medication B", quantity: 5 }
    ];
  </script>
  
  <h2>Medication List</h2>
  
  <ul>
    {#each medications as medication}
      <li>{medication.name} - Quantity: {medication.quantity}</li>
    {/each}
  </ul>
  