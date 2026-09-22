# KeyNest — Odoo Practice Tasks for Real Estate Agencies

*"From listing to closed deal."*

A set of practice tasks for building a real estate management module in Odoo. Each task is written like a real client request, not a coding exercise. Build it, then record it if you're making a portfolio video.

## How to use this file

1. Start from Easy, move to Medium, then try Hard once you're comfortable.
2. Read the "Scenario" like it's an actual client sitting in front of you. That's the real skill — turning a vague request into a working system.
3. Some tasks say **Depends on** — do that task first, since the next one builds on it.
4. Tasks marked **Full Cycle** need 3-4 modules working together. These are the best ones to show in a video because they prove you understand how Odoo modules connect, not just isolated fixes.

## Difficulty guide

- 🟢 **Easy** — one module, basic configuration, good for warming up
- 🟡 **Medium** — one or two modules, some automation or logic, this is where most real work lives
- 🔴 **Hard** — three or more modules, real business logic, reporting across branches

---

### 🟢 R1. Property Listing Catalog
**Modules:** Sales

**Scenario:** The agency lists properties for sale by area, size, and number of rooms, and wants a proper catalog instead of a shared spreadsheet.

**What to build:** Set up properties as products with variants for size and rooms. Add photos. Set a pricelist that varies by city.

**Goal:** Agents pull up a clean catalog by city or size instead of scrolling a spreadsheet.

---

### 🟢 R2. Owner, Tenant, and Buyer Contacts
**Modules:** Contacts

**Scenario:** The agency's contact list mixes property owners, tenants, and buyers together with no way to tell them apart quickly.

**What to build:** Create tags for Owner, Tenant, and Buyer. Build filtered views for each type.

**Goal:** Staff can pull up "all owners" or "all buyers" in one click.

---

### 🟡 R3. Buyer Lead Pipeline
**Modules:** CRM

**Scenario:** The agency loses track of buyers after a site visit — some just disappear and nobody follows up on why.

**What to build:** Build a pipeline: New Lead → Site Visit Scheduled → Negotiation → Sold / Lost. Require a reason whenever a deal is marked Lost.

**Goal:** Management can see exactly why deals are being lost — price, location, financing, etc. — instead of just losing the lead silently.

---

### 🟡 R4. Site Visit Scheduling Without Agent Conflicts
**Modules:** Calendar, CRM

**Scenario:** Two clients were once sent to the same agent for a visit at the same time by mistake.

**What to build:** Link site visits to the CRM opportunity and to the agent's calendar so a new visit can't be booked if that agent is already busy.

**Goal:** Agent double-booking is prevented automatically.

**Depends on:** R3

---

### 🟡 R5. Rental Contracts with Recurring Invoices
**Modules:** Sales, Accounting

**Scenario:** For rented properties, staff currently create a new invoice manually every single month, which is slow and sometimes forgotten.

**What to build:** Set up a recurring monthly invoice for each rental contract that generates automatically without anyone touching it.

**Goal:** Rent invoices appear on time every month with zero manual work.

---

### 🟡 R6. Agent Commission Calculation
**Modules:** Employees, Accounting

**Scenario:** Agents are paid a commission based on the value of properties they sell, but it's currently calculated by hand on a calculator each month.

**What to build:** Calculate commission as a percentage of the sold property's price and feed it into the agent's payslip as an input line automatically.

**Goal:** Commission shows up correctly on the payslip without manual math.

**Depends on:** R3

---

### 🟡 R7. Property Maintenance Requests
**Modules:** Maintenance

**Scenario:** Tenants report broken things (AC, plumbing) by calling the office, and requests get lost or forgotten.

**What to build:** Set up a maintenance request flow: tenant issue reported → assigned to a technician → cost logged → marked resolved.

**Goal:** Every maintenance issue is tracked from report to fix, with a cost history per property.

---

### 🟡 R8. Legal Document Approval Before Sale Closes
**Modules:** Approvals

**Scenario:** A property was once sold before the legal paperwork was actually verified, causing a big problem.

**What to build:** Build an approval flow requiring the legal team to approve the document before a sale can be marked as closed.

**Goal:** A sale cannot be closed without legal sign-off — no more skipped steps.

---

### 🟡 R9. Full Cycle — Lead to Sold Property
**Modules:** CRM, Sales, Accounting

**Scenario:** From first phone call to signed contract, the agency wants one trail they can look back on for any property sale.

**What to build:** Lead enters CRM → site visit scheduled → offer becomes a sale order → invoice generated and paid → commission calculated for the agent.

**Goal:** One property sale, one continuous record from first contact to paid commission.

**Depends on:** R3, R5, R6

---

### 🔴 R10. Multi-Agency Performance Report
**Modules:** Accounting, CRM, Employees

**Scenario:** A real estate company runs 3 branch offices and wants to compare which branch and which agents are actually performing best.

**What to build:** Build a report comparing revenue, number of deals closed, and commissions paid per branch and per agent, side by side.

**Goal:** Owner sees exactly which branch and which agent is driving the most business, in one view.

---

## Best task for your portfolio video

**R9 — Full Cycle: Lead to Sold Property** is the strongest pick for KeyNest. It proves you can connect CRM, Sales, and Accounting into one working deal flow — not just fix one isolated bug.
