// Currency conversion rates (approximate)
const USD_TO_INR = 83.5;

// Currency formatting based on location
function formatCurrency(priceUSD, location) {
    if (location.includes('India')) {
        const priceINR = priceUSD * USD_TO_INR;
        return new Intl.NumberFormat('en-IN', {
            style: 'currency',
            currency: 'INR',
            maximumFractionDigits: 0
        }).format(priceINR);
    } else {
        return new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'USD',
            maximumFractionDigits: 0
        }).format(priceUSD);
    }
}

document.getElementById('predictionForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const predictBtn = document.getElementById('predictBtn');
    const resultValue = document.getElementById('resultValue');
    const locationDisplay = document.getElementById('locationDisplay');
    const loading = document.getElementById('loading');
    const errorMsg = document.getElementById('errorMsg');

    // Reset UI
    errorMsg.textContent = '';
    resultValue.textContent = 'Calculating...';
    resultValue.style.color = 'var(--text-color)';
    loading.style.display = 'block';
    predictBtn.disabled = true;

    // Collect form data
    const location = document.getElementById('Location').value;
    const formData = {
        Location: location,
        MedInc: parseFloat(document.getElementById('MedInc').value),
        HouseAge: parseInt(document.getElementById('HouseAge').value),
        AveRooms: parseFloat(document.getElementById('AveRooms').value),
        AveBedrms: parseFloat(document.getElementById('AveBedrms').value),
        Population: parseInt(document.getElementById('Population').value),
        AveOccup: parseFloat(document.getElementById('AveOccup').value),
        Latitude: parseFloat(document.getElementById('Latitude').value),
        Longitude: parseFloat(document.getElementById('Longitude').value)
    };

    try {
        const response = await fetch('https://ai-house-price-predictor-9i6h.onrender.com', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData),
        });

        const data = await response.json();

        if (response.ok) {
            // Format price based on location currency
            const formatted = formatCurrency(data.price_usd, location);

            resultValue.textContent = formatted;
            resultValue.style.color = 'var(--accent-color)';

            // Show currency type in location display
            const currencyType = location.includes('India') ? '🇮🇳 INR' : '🇺🇸 USD';
            locationDisplay.textContent = `${data.location} (${currencyType})`;
        } else {
            throw new Error(data.error || 'Prediction failed');
        }
    } catch (err) {
        errorMsg.textContent = `Error: ${err.message}. Ensure backend is running.`;
        resultValue.textContent = '---';
        resultValue.style.color = 'var(--error-color)';
    } finally {
        loading.style.display = 'none';
        predictBtn.disabled = false;
    }
});

// Update location display on change
document.getElementById('Location').addEventListener('change', (e) => {
    const location = e.target.value;
    const currencyType = location.includes('India') ? '🇮🇳 INR' : '🇺🇸 USD';
    document.getElementById('locationDisplay').textContent = `Currency: ${currencyType}`;
});
