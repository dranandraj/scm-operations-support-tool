document.addEventListener("DOMContentLoaded", function () {

    
    // ==========================================
    // CUSTOMER FORM VALIDATION
    // ==========================================

    const customerForm = document.querySelector(
        'form input[name="customer_name"]'
    )?.closest("form");

    if (customerForm) {

        customerForm.noValidate = true;

        const customerId = customerForm.querySelector(
            'input[name="customer_id"]'
        );

        const customerName = customerForm.querySelector(
            'input[name="customer_name"]'
        );

        const country = customerForm.querySelector(
            'select[name="country"]'
        );

        const status = customerForm.querySelector(
            'select[name="status"]'
        );


        [
            customerId,
            customerName,
            country,
            status
        ].forEach(function (field) {

            if (field) {

                field.addEventListener("input", function () {
                    field.setCustomValidity("");
                    field.classList.remove("is-invalid");
                });

                field.addEventListener("change", function () {
                    field.setCustomValidity("");
                    field.classList.remove("is-invalid");
                });

            }

        });


        customerForm.addEventListener("submit", function (event) {

            let isValid = true;


            [
                customerId,
                customerName,
                country,
                status
            ].forEach(function (field) {

                if (field) {
                    field.setCustomValidity("");
                    field.classList.remove("is-invalid");
                }

            });


            if (customerId && customerId.value.trim() === "") {

                customerId.setCustomValidity(
                    "Customer ID is required."
                );

                customerId.classList.add("is-invalid");

                isValid = false;
            }


            if (customerName && customerName.value.trim() === "") {

                customerName.setCustomValidity(
                    "Customer name is required."
                );

                customerName.classList.add("is-invalid");

                isValid = false;
            }


            if (country && country.value === "") {

                country.setCustomValidity(
                    "Please select a country."
                );

                country.classList.add("is-invalid");

                isValid = false;
            }


            if (status && status.value === "") {

                status.setCustomValidity(
                    "Please select a status."
                );

                status.classList.add("is-invalid");

                isValid = false;
            }


            if (!isValid) {

                event.preventDefault();

                customerForm.reportValidity();
            }

        });

    }


    // ==========================================
    // MATERIAL FORM VALIDATION
    // ==========================================

    const materialForm = document.querySelector(
        'form input[name="material_name"]'
    )?.closest("form");

    if (materialForm) {

        materialForm.noValidate = true;

        const materialId = materialForm.querySelector(
            'input[name="material_id"]'
        );

        const materialName = materialForm.querySelector(
            'input[name="material_name"]'
        );

        const category = materialForm.querySelector(
            'select[name="category"]'
        );

        const plant = materialForm.querySelector(
            'select[name="plant"]'
        );

        const price = materialForm.querySelector(
            'input[name="price"]'
        );

        const status = materialForm.querySelector(
            'select[name="status"]'
        );


        [
            materialId,
            materialName,
            category,
            plant,
            price,
            status
        ].forEach(function (field) {

            if (field) {

                field.addEventListener("input", function () {
                    field.setCustomValidity("");
                    field.classList.remove("is-invalid");
                });

                field.addEventListener("change", function () {
                    field.setCustomValidity("");
                    field.classList.remove("is-invalid");
                });

            }

        });


        materialForm.addEventListener("submit", function (event) {

            let isValid = true;


            [
                materialId,
                materialName,
                category,
                plant,
                price,
                status
            ].forEach(function (field) {

                if (field) {
                    field.setCustomValidity("");
                    field.classList.remove("is-invalid");
                }

            });


            if (materialId && materialId.value.trim() === "") {

                materialId.setCustomValidity(
                    "Material ID is required."
                );

                materialId.classList.add("is-invalid");

                isValid = false;
            }


            if (materialName && materialName.value.trim() === "") {

                materialName.setCustomValidity(
                    "Material name is required."
                );

                materialName.classList.add("is-invalid");

                isValid = false;
            }


            if (category && category.value === "") {

                category.setCustomValidity(
                    "Please select a category."
                );

                category.classList.add("is-invalid");

                isValid = false;
            }


            if (plant && plant.value === "") {

                plant.setCustomValidity(
                    "Please select a plant."
                );

                plant.classList.add("is-invalid");

                isValid = false;
            }


            if (price) {

                const priceValue = price.value.trim();

                if (priceValue === "") {

                    price.setCustomValidity(
                        "Price is required."
                    );

                    price.classList.add("is-invalid");

                    isValid = false;

                } else if (Number(priceValue) < 0) {

                    price.setCustomValidity(
                        "Price cannot be negative."
                    );

                    price.classList.add("is-invalid");

                    isValid = false;
                }

            }


            if (status && status.value === "") {

                status.setCustomValidity(
                    "Please select a status."
                );

                status.classList.add("is-invalid");

                isValid = false;
            }


            if (!isValid) {

                event.preventDefault();

                materialForm.reportValidity();
            }

        });

    }


    // ==========================================
    // SALES ORDER FORM VALIDATION
    // ==========================================

    const salesOrderForm = document.querySelector(
        'form input[name="order_id"]'
    )?.closest("form");

    if (salesOrderForm) {

        salesOrderForm.noValidate = true;

        const orderId = salesOrderForm.querySelector(
            'input[name="order_id"]'
        );

        const salesCustomerId = salesOrderForm.querySelector(
            'select[name="customer_id"]'
        );

        const salesMaterialId = salesOrderForm.querySelector(
            'select[name="material_id"]'
        );

        const quantity = salesOrderForm.querySelector(
            'input[name="quantity"]'
        );

        const salesStatus = salesOrderForm.querySelector(
            'select[name="status"]'
        );

        const orderDate = salesOrderForm.querySelector(
            'input[name="order_date"]'
        );


        [
            orderId,
            salesCustomerId,
            salesMaterialId,
            quantity,
            salesStatus,
            orderDate
        ].forEach(function (field) {

            if (field) {

                field.addEventListener("input", function () {
                    field.setCustomValidity("");
                    field.classList.remove("is-invalid");
                });

                field.addEventListener("change", function () {
                    field.setCustomValidity("");
                    field.classList.remove("is-invalid");
                });

            }

        });


        salesOrderForm.addEventListener("submit", function (event) {

            let isValid = true;


            [
                orderId,
                salesCustomerId,
                salesMaterialId,
                quantity,
                salesStatus,
                orderDate
            ].forEach(function (field) {

                if (field) {
                    field.setCustomValidity("");
                    field.classList.remove("is-invalid");
                }

            });


            if (orderId && orderId.value.trim() === "") {

                orderId.setCustomValidity(
                    "Sales Order ID is required."
                );

                orderId.classList.add("is-invalid");

                isValid = false;
            }


            if (salesCustomerId && salesCustomerId.value === "") {

                salesCustomerId.setCustomValidity(
                    "Please select a customer."
                );

                salesCustomerId.classList.add("is-invalid");

                isValid = false;
            }


            if (salesMaterialId && salesMaterialId.value === "") {

                salesMaterialId.setCustomValidity(
                    "Please select a material."
                );

                salesMaterialId.classList.add("is-invalid");

                isValid = false;
            }


            if (quantity) {

                const quantityValue = quantity.value.trim();

                if (quantityValue === "") {

                    quantity.setCustomValidity(
                        "Quantity is required."
                    );

                    quantity.classList.add("is-invalid");

                    isValid = false;

                } else if (Number(quantityValue) <= 0) {

                    quantity.setCustomValidity(
                        "Quantity must be greater than 0."
                    );

                    quantity.classList.add("is-invalid");

                    isValid = false;
                }

            }


            if (salesStatus && salesStatus.value === "") {

                salesStatus.setCustomValidity(
                    "Please select a status."
                );

                salesStatus.classList.add("is-invalid");

                isValid = false;
            }


            if (orderDate && orderDate.value === "") {

                orderDate.setCustomValidity(
                    "Order date is required."
                );

                orderDate.classList.add("is-invalid");

                isValid = false;
            }


            if (!isValid) {

                event.preventDefault();

                salesOrderForm.reportValidity();
            }

        });

    }


    // ==========================================
    // SUPPORT REQUEST FORM VALIDATION
    // ==========================================

    const supportRequestForm = document.querySelector(
        'form textarea[name="description"]'
    )?.closest("form");

    if (supportRequestForm) {

        supportRequestForm.noValidate = true;

        const requestId = supportRequestForm.querySelector(
            'input[name="request_id"]'
        );

        const issueType = supportRequestForm.querySelector(
            'input[name="issue_type"]'
        );

        const description = supportRequestForm.querySelector(
            'textarea[name="description"]'
        );

        const supportStatus = supportRequestForm.querySelector(
            'select[name="status"]'
        );

        const createdDate = supportRequestForm.querySelector(
            'input[name="created_date"]'
        );


        // Clear validation message when user edits a field
        [
            requestId,
            issueType,
            description,
            supportStatus,
            createdDate
        ].forEach(function (field) {

            if (field) {

                field.addEventListener("input", function () {
                    field.setCustomValidity("");
                    field.classList.remove("is-invalid");
                });

                field.addEventListener("change", function () {
                    field.setCustomValidity("");
                    field.classList.remove("is-invalid");
                });

            }

        });


        // Support Request submit validation
        supportRequestForm.addEventListener("submit", function (event) {

            let isValid = true;


            // Clear previous validation
            [
                requestId,
                issueType,
                description,
                supportStatus,
                createdDate
            ].forEach(function (field) {

                if (field) {
                    field.setCustomValidity("");
                    field.classList.remove("is-invalid");
                }

            });


            // Request ID
            // On Edit page this field is readonly,
            // so validation will only matter if it is empty.
            if (requestId && requestId.value.trim() === "") {

                requestId.setCustomValidity(
                    "Request ID is required."
                );

                requestId.classList.add("is-invalid");

                isValid = false;
            }


            // Issue Type
            if (issueType && issueType.value.trim() === "") {

                issueType.setCustomValidity(
                    "Issue type is required."
                );

                issueType.classList.add("is-invalid");

                isValid = false;
            }


            // Description
            if (description && description.value.trim() === "") {

                description.setCustomValidity(
                    "Description is required."
                );

                description.classList.add("is-invalid");

                isValid = false;
            }


            // Status
            if (supportStatus && supportStatus.value === "") {

                supportStatus.setCustomValidity(
                    "Please select a status."
                );

                supportStatus.classList.add("is-invalid");

                isValid = false;
            }


            // Created Date
            if (createdDate && createdDate.value === "") {

                createdDate.setCustomValidity(
                    "Created date is required."
                );

                createdDate.classList.add("is-invalid");

                isValid = false;
            }


            // Stop submission if validation fails
            if (!isValid) {

                event.preventDefault();

                supportRequestForm.reportValidity();
            }

        });

    }

});

// ==========================================
// Dynamic Notifications
// ==========================================

document.addEventListener("DOMContentLoaded", function () {

    const alerts = document.querySelectorAll(".alert");

    alerts.forEach(function (alert) {

        // Keep the notification visible for 4 seconds
        setTimeout(function () {

            alert.style.transition = "opacity 0.5s ease";
            alert.style.opacity = "0";

            // Remove the notification after fade-out
            setTimeout(function () {
                alert.remove();
            }, 500);

        }, 4000);

    });

});

// ==========================================
// Dashboard KPI Count-up Animation
// ==========================================

document.addEventListener("DOMContentLoaded", function () {
    const counters = document.querySelectorAll(".dashboard-card h3");

    counters.forEach(function (counter) {
        const target = parseInt(counter.textContent.trim(), 10);

        // Skip if the element does not contain a valid number
        if (Number.isNaN(target) || target < 0) {
            return;
        }

        const duration = 800; // Animation duration in milliseconds
        const startTime = performance.now();

        counter.textContent = "0";

        function updateCounter(currentTime) {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);

            const currentValue = Math.floor(progress * target);

            counter.textContent = currentValue.toLocaleString();

            if (progress < 1) {
                requestAnimationFrame(updateCounter);
            } else {
                counter.textContent = target.toLocaleString();
            }
        }

        requestAnimationFrame(updateCounter);
    });
});