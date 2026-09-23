# KeyNest - Odoo Practice Tasks for Real Estate Agencies

*"From listing to closed deal."*

These are practice tasks for building a real estate management module in Odoo. I wrote every task the way a real client would ask for it, so don't expect a click-by-click tutorial. Figuring out what the client actually needs is part of the work.

Build it, test it, and if you're making a portfolio video, record it.

## Before you start

- Create a custom module called `keynest` and put all your work inside it.
- Even when a task is mostly setup (tags, stages, pricelists), try to save that setup in your module as XML or CSV data files. My test is simple: I install your module on a new, empty database and your work should be there. Anything you only clicked in the UI is gone with the database.
- Each task has an **Apps** line. Install those apps before you start the task.
- If you don't see an app called **Accounting**, use **Invoicing**. It covers everything these tasks need.
- Menu names and settings move around a bit between Odoo versions. If a hint points to something you can't find in your version, look for the same feature under a different name.
- Create some test data before testing: a few properties, 2 or 3 agents (employees with a user), and some customers.

## How to read each task

- **Scenario** - the problem, the way the client explains it to you. Read it like the client is sitting in front of you.
- **What to build** - what I expect you to deliver.
- **Done when** - the checklist I'll use to test your work. If every point works, the task is done.
- **Hints** - where to look in Odoo. Only read them if you're stuck.
- **Goal** - what the client gets out of it. If your solution works but doesn't reach the goal, it's not finished.
- **Depends on** - finish that task first, because this one builds on it.

If something is not clear, make a reasonable decision, write it down in a short note, and keep going. That's what you'd do with a real client too.

## Difficulty

- 🟢 **Easy** - one app, mostly configuration. Good for warming up.
- 🟡 **Medium** - one or two apps, with some automation or custom logic. Most real client work looks like this.
- 🔴 **Hard** - three or more apps, real business logic, and reporting across branches.

## Suggested order

R2 → R1 → R3 → R4 → R7 → R5 → R8 → R6 → R9 → R10 → R11

---

### 🟢 R1. Property Listing Catalog
**Apps:** Sales

**Scenario:** The agency lists properties for sale by area, size, and number of rooms. Right now everything is in a shared spreadsheet and they want a proper catalog instead.

**What to build:**
1. Set up the properties as products.
2. Use product variants for size and number of rooms. For example, one listing could have a 120 m² / 3 rooms variant and a 150 m² / 4 rooms variant.
3. Add photos to the properties.
4. Create a pricelist where the price changes depending on the city.

**Done when:**
- The properties show up in Sales as products, with photos.
- Size and rooms are variants you can choose from, not free text.
- An agent can filter or group the catalog by city and by size.
- On a quotation, picking the pricelist for a city changes the property price.

**Hints:**
- Turn on **Variants** and **Pricelists** in Sales > Configuration > Settings first.
- Products have no "city" field by default. How you store the city is your call (a field, a category, a tag...). Just make sure agents can filter by it.

**Goal:** Agents pull up a clean catalog by city or size instead of scrolling a spreadsheet.

---

### 🟢 R2. Owner, Tenant, and Buyer Contacts
**Apps:** Contacts

**Scenario:** The agency's contact list mixes property owners, tenants, and buyers together, and there's no quick way to tell them apart.

**What to build:**
1. Create three contact tags: **Owner**, **Tenant**, and **Buyer**.
2. Add a ready-made filter for each type so staff don't have to build the filter by hand every time.

**Done when:**
- The Contacts screen has one-click filters for Owners, Tenants, and Buyers.
- One person can have more than one tag (for example someone who owns a flat and rents another one), and they show up in both lists.
- The filters are still there after installing the module on a new database.

**Hints:**
- A filter saved as a Favorite only lives in your database. Add the filters to the contacts search view from your module, or add menu items that open contacts with the right filter.

**Goal:** Staff can pull up "all owners" or "all buyers" in one click.

---

### 🟡 R3. Buyer Lead Pipeline
**Apps:** CRM

**Scenario:** The agency loses track of buyers after a site visit. Some of them just disappear and nobody follows up to find out why.

**What to build:**
1. A CRM pipeline with these stages, in this order: **New Lead → Site Visit Scheduled → Negotiation → Sold**.
2. A way to mark a deal as **Lost**. You can use Odoo's built-in "Lost" button or your own stage, but read point 3 first.
3. A reason is **required** every time a deal is marked Lost. Add lost reasons that fit a real estate agency: Price, Location, Financing, and any others you think make sense.

**Done when:**
- The pipeline shows the 4 stages in the right order.
- Marking a deal as Lost without a reason is blocked.
- Marking it Lost with a reason works, and the reason is saved on the deal.
- A manager can open a report of lost deals grouped by reason.

**Hints:**
- Look at what Odoo does by default when you click "Lost" and see what's missing compared to what the client asked for.

**Goal:** Management can see exactly why deals are being lost (price, location, financing, etc.) instead of leads quietly disappearing.

---

### 🟡 R4. Site Visit Scheduling Without Agent Conflicts
**Apps:** Calendar, CRM
**Depends on:** R3

**Scenario:** Once, two clients were sent to the same agent for a visit at the same time by mistake.

**What to build:**
1. Site visits are calendar events created from the CRM opportunity, so each visit is linked to its deal.
2. Each visit is assigned to an agent and shows up in that agent's calendar.
3. When someone books a visit, the system checks the agent's calendar. If the agent already has something at that time, the booking is refused with a clear message.

**Done when:**
- You can create a visit from an opportunity. It shows on the opportunity and in the agent's calendar.
- Book agent A from 10:00 to 11:00, then try to book agent A from 10:30 to 11:30. It's blocked, and the message says why.
- Agent B can be booked at 10:30 with no problem.
- A visit starting at 11:00, right after one that ends at 11:00, is allowed.
- Dragging an existing visit into a busy slot on the calendar is also blocked.

**Hints:**
- "Busy" means anything already on the agent's calendar, not only other site visits.
- This needs Python code. Configuration alone won't do it.

**Goal:** Agent double-booking is prevented automatically.

---

### 🟡 R5. Rental Contracts with Recurring Invoices
**Apps:** Sales, Accounting

**Scenario:** For rented properties, staff create a new invoice by hand every single month. It's slow, and sometimes they forget.

**What to build:**
1. A rental contract for each rented property, with the monthly rent and the tenant.
2. A recurring monthly invoice that is created automatically for each contract, without anyone touching it.

**Done when:**
- You confirm a rental contract and the first invoice is created.
- The next month's invoice gets created by the system on its own date. Nobody clicks anything.
- The contract shows when the next invoice will be created.
- Stopping or closing the contract stops the invoices.

**Hints:**
- Check if your Odoo has an app for recurring sales or recurring invoices. If it doesn't, a scheduled action that creates the monthly invoice from the contract does the same job.
- To test without waiting a month, run the scheduled action by hand (Settings > Technical > Scheduled Actions, needs developer mode).

**Goal:** Rent invoices show up on time every month with zero manual work.

---

### 🟡 R6. Agent Commission Calculation
**Apps:** Employees, Accounting (plus Payroll)
**Depends on:** R3

**Scenario:** Agents earn a commission based on the value of the properties they sell. Right now someone works it out on a calculator every month.

**What to build:**
1. Calculate each agent's commission as a percentage of the price of the properties they sold.
2. Put that amount on the agent's payslip automatically, as an input line.

**Done when:**
- An agent sells a property for 1,000,000 with a 2% rate, and their commission is 20,000.
- When you generate the payslip for that month, the commission line is already there with the right amount. Nobody types it in.
- An agent with no sales that month gets no commission (or 0).
- Only sales from that payslip's period are counted.

**Hints:**
- Payslips come from a Payroll app. Any payroll module works. If your Odoo doesn't have one, there are free payroll modules on the Odoo Apps store and from the OCA.
- You decide where the percentage is stored (per agent, one rate for the whole company...). Write down what you chose.
- You also decide which amount counts as "the property's price". The confirmed sale order total is the usual choice.

**Goal:** Commission shows up correctly on the payslip without any manual math.

---

### 🟡 R7. Property Maintenance Requests
**Apps:** Maintenance

**Scenario:** Tenants call the office when something breaks (AC, plumbing...). The requests get lost or forgotten.

**What to build:** A maintenance request flow with these steps:
1. **Reported** - staff log the issue, the property, and the tenant who called.
2. **Assigned** - the request goes to a technician.
3. **Cost logged** - the cost of the repair is recorded on the request.
4. **Resolved** - the request is closed.

**Done when:**
- You can create a request linked to a property and a tenant.
- You can assign a technician and they can see their requests.
- You can enter a cost on the request.
- Opening a property shows all its maintenance requests and the total cost so far.

**Hints:**
- In the Maintenance app, "equipment" can stand for a property. Think about whether that fits or whether you'd rather link requests to the property another way.
- Check if a cost field already exists before you add one.

**Goal:** Every maintenance issue is tracked from report to fix, with a cost history for each property.

---

### 🟡 R8. Legal Document Approval Before Sale Closes
**Apps:** Approvals

**Scenario:** Once, a property was sold before anyone checked the legal paperwork, and it caused a big problem.

**What to build:**
1. An approval type for legal document review, where the legal team is the approver.
2. Each sale gets its own approval request, linked to that sale.
3. The sale can't be closed until the legal approval is approved.

**Done when:**
- Trying to close a sale with no approved legal review is blocked, and the message says why.
- After the legal team approves, closing the sale works.
- If the legal team refuses, the sale still can't be closed.
- Only people in the legal team can approve.

**Hints:**
- If you don't have the Approvals app, build a simple approval step yourself (a status on the sale that only the legal team can change).
- First decide where a sale "closes" in your setup: confirming the sale order, or moving the deal to Sold (if you did R3). Then block that step.

**Goal:** A sale can't be closed without legal sign-off. No more skipped steps.

---

### 🟡 R9. Full Cycle - Lead to Sold Property
**Apps:** CRM, Sales, Accounting
**Depends on:** R3, R5, R6

**Scenario:** The agency wants one trail they can look back on for any property sale, from the first phone call to the signed contract.

**What to build:** Connect these steps so each one comes from the one before it:
1. A lead comes into CRM.
2. A site visit is scheduled from the lead.
3. The offer becomes a sale order (quotation from the opportunity, then confirmed).
4. An invoice is created from the sale order and gets paid.
5. The agent's commission is calculated from that sale.

**Done when:**
- You can run one property from lead to paid commission without typing the same data twice.
- From the opportunity, you can open the sale order, the invoice, and the payment.
- The commission for that sale shows up on the agent's payslip.

**Hints:**
- Most of these links already exist in Odoo. Your job is to make sure nothing breaks between the steps and to fill any gaps.
- This is a great one to record. Show one property going through the whole flow.

**Goal:** One property sale, one continuous record, from first contact to paid commission.

---

### 🔴 R10. Multi-Agency Performance Report
**Apps:** Accounting, CRM, Employees

**Scenario:** A real estate company runs 3 branch offices. The owner wants to compare which branch, and which agents, are actually performing best.

**What to build:**
1. Set up the 3 branches. You choose how (separate companies, sales teams, or analytic accounts), and explain why you picked it.
2. A report that shows these numbers side by side, per branch and per agent:
   - Revenue
   - Number of deals closed
   - Commissions paid

**Done when:**
- The owner opens one screen and sees all 3 branches next to each other.
- They can drill down from a branch to its agents.
- They can filter by period (this month, this quarter, this year).
- The numbers match the actual invoices and payslips.

**Hints:**
- Pivot and graph views go a long way. If they're not enough, look at dashboards/spreadsheets or a custom report model.

**Goal:** The owner sees exactly which branch and which agent brings in the most business, in one view.

---
### 🔴 R11. Property Installment Plans
**Apps:** Sales, Accounting
**Depends on:** R1

**Why this task:** Almost every agency that sells new or off-plan units sells them on installments. Odoo can split one invoice into a few payment dates, but it has nothing for a real installment plan that runs for years.

**Scenario:** Most buyers don't pay cash. They pay a down payment, then an installment every quarter for 3 to 7 years. Right now the accountant keeps a separate Excel sheet for every buyer. Nobody can tell quickly who is late, how much is still owed on a unit, or how much money is coming in next month.

**What to build:**
1. An **installment plan** you attach to a property sale, with:
   - Down payment (amount or %)
   - Number of installments
   - How often (monthly, quarterly, yearly)
   - Start date
2. From the plan, the system generates the full **schedule**: one line per installment with its due date, amount, and status (Not due, Due, Paid, Late).
3. Each installment becomes its own invoice when it's due, not all at once on day one.
4. A **late fee** when an installment is paid late. You decide how it's calculated (fixed amount or %) and write it down.
5. A **collections view**: all installments due this month and all late ones, across all buyers.

**Done when:**
- A 1,000,000 sale with 20% down and 8 quarterly installments creates 1 down payment line and 8 installments of 100,000, with the right dates.
- The installment invoices get created on their own as their dates come.
- Paying an invoice marks that installment Paid. An unpaid one past its date shows Late.
- On the sale you can see at a glance: total paid, total remaining, next installment date.
- The accountant can open one screen and see who owes what this month and who is late.
- The Excel sheet isn't needed anymore.

**Hints:**
- Keep the plan and its lines as your own models linked to the sale order. Don't try to force this into payment terms.
- Rounding matters. Make sure the installments add up to exactly the total, even when it doesn't divide evenly.

**Goal:** The agency tracks every buyer's installments in Odoo, knows who is late without digging, and can see the money coming in over the next months.

---

## Best task for your portfolio video

Pick **R9 - Full Cycle: Lead to Sold Property**. It shows CRM, Sales, and Accounting working together as one deal flow, which is exactly what clients hire an Odoo developer for.

## What to hand in

- Your `keynest` module (it should install on a new database without errors).
- A short note with any decisions you made where the task left the choice to you.
- Optional: a short video of the task working.
