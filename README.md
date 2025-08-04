# 🏠 Property Management System

An Odoo 18 custom module designed to manage properties, tenants, lease contracts, rent payments, and analytics with automation and reporting features.

---

## 📌 Overview

This module is a **capstone project** by **Abeza Getachew**, built to streamline the workflow for property owners, agents, and managers. It simplifies lease tracking, rent collection, document generation, and includes role-based access control for secure usage.

---

## 🚀 Features

### ✅ Property Management
- Add properties with type, status, price, description, and images
- Track property availability and status changes (available, rented, maintenance)

### ✅ Tenant Management
- Store tenant info: name, contact, ID number
- Track tenant lease history

### ✅ Lease Management
- Draft → Active → Expired state management
- Auto-generate lease name as "Tenant Name - Property Name"
- Date constraints to prevent overlapping leases
- Smart auto-fill monthly rent from property
- Inline rent payment tracking inside lease form
- Lease PDF generation using QWeb

### ✅ Rent Payment Tracking
- Record payments by lease
- Status tracking (paid/unpaid)
- Notes and payment history

### ✅ Reporting & Analytics
- 📄 **QWeb PDF**: Lease Summary Report
- 📊 **Graph View**:
  - Rent collection over time
  - Active leases per property type
- 📁 **Excel Export**:
  - Lease summary using `xlsxwriter`
- 🧱 **Kanban View**: Lease pipeline with color-coded stages

### ✅ Automation
- Auto-update property status when leased
- Cron job to send lease-expiry reminders (30 days in advance)

---

## 🔐 Access & Security

- **Groups**:
  - Property Manager: Full access
  - Accountant: Can view payments
- **Access Rules**:
  - Only managers can create/update leases & properties
  - (Optional) Portal user access for tenants to view their leases/payments

---

## 🧩 Models

- `property.management.property`
- `property.management.tenant`
- `property.management.lease`
- `property.management.rent_payment`

---

## 🖥️ Installation

1. Place the module folder inside your Odoo custom addons directory.
2. Update the apps list from the Odoo backend.
3. Search for **Property Management** and install the module.

---

## 🛠️ Tech Stack

- Odoo 18
- Python
- PostgreSQL
- QWeb Reporting
- XLSXWriter (for Excel export)
- XML views, statusbar, widgets

---

## 📸 Screenshots

*(Include screenshots of List View, Form View, Reports, Kanban if available)*

---

## 📃 License

This project is for academic and demonstration purposes only.

---

## 🙋‍♂️ Author

**Abeza Getachew**  
Odoo Developer | Junior IT Officer  
📧 abezagetsc@gmail.com  
🌍 Addis Ababa, Ethiopia  
[GitHub](https://github.com/AbezaGetachew)

---

