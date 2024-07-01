# Backend for TODO app

### Testing Stripe locally (`stripe cli` installed required)
1. `$ stripe login`
2. `$ stripe listen --forward-to localhost:8000/checkout/webhook/`
3. `$ stripe trigger payment_intent.succeeded`