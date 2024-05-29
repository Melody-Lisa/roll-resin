var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Sedan", serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#6c757d'
        },
        backgroundColor: '#fff',
        padding: '10px 12px',
        border: '1px solid #6c757d',
        borderRadius: '4px', // Add border radius
        boxShadow: '0 0 10px rgba(0, 0, 0, 0.1)',
    },
    invalid: {
        color: 'red',
        iconColor: 'red'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');