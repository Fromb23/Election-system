function showStep(step) {
	if (step === 2) {
		// Ensure both checkboxes are checked
		const consentSignature = document.getElementById('consentSignature').checked;
		const privacyAct = document.getElementById('privacyAct').checked;
		if (!consentSignature || !privacyAct) {
			alert('You must agree to both requirements to proceed to Step 2');
			return; // Stop execution if checkboxes are not checked
		}
	}

	// Remove 'active' class from both buttons and hide content
	document.getElementById('btnStep1').classList.remove('active');
	document.getElementById('btnStep2').classList.remove('active');
	document.getElementById('contentStep1').style.display = 'none';
	document.getElementById('contentStep2').style.display = 'none';

	// Show appropriate content and set active button
	if (step === 1) {
		document.getElementById('btnStep1').classList.add('active');
		document.getElementById('contentStep1').style.display = 'block';
	} else if (step === 2) {
		document.getElementById('btnStep2').classList.add('active');
		document.getElementById('contentStep2').style.display = 'block';
	}
}
