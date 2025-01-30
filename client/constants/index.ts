export const GenderOptions = ["male", "female"]

export const PatientFormDefaultValues = {
    firstName: "",
    lastName: "",
    email: "",
    phone: "",
    birthDate: new Date(Date.now()),
    gender: "male" as Gender,
    address: "",
    occupation: "",
    emergencyContactName: "",
    emergencyContactNumber: "",
    primaryPhysician: "",
    insuranceProvider: "",
    insurancePolicyNumber: "",
    allergies: "",
    currentMedication: "",
    familyMedicalHistory: "",
    pastMedicalHistory: "",
    identificationType: "Cédula de Identidad",
    identificationNumber: "",
    identificationDocument: [],
    treatmentConsent: false,
    disclosureConsent: false,
    privacyConsent: false,
};

export const IdentificationTypes = [
    "Cédula de Identidad",
    "Pasaporte",
    "Licencia de Conducir",
    "Carné de Seguro Médico",
    "Tarjeta de Identificación Militar",
    "Tarjeta de Identificación de Estudiante",
    "Tarjeta de Identificación de Votante",
    "Certificado de Nacimiento",
    "Carné de Residencia (para extranjeros)"
];

export const Doctors = [
    {
        image: "/assets/images/dr-tiban.png",
        name: "Danilo Tiban - Medicina General - Ecografía", 
    },
    {
        image: "/assets/images/dr-acosta.png",
        name: "Alfonso Acosta - Urología",
    },
    {
        image: "/assets/images/dr-carvajal.png",
        name: "Nataly Carvajal - Laboratorio Clínico",
    },
    {
        image: "/assets/images/dr-diaz.png",
        name: "Mary Diaz - Psicológia Clínica", 
    },
    {
        image: "/assets/images/lic-robalino.png",
        name: "Darwin Robalino - Fisiología y Rehabilitación",
    },
    {
        image: "/assets/images/dr-telenchana.png",
        name: "Rosa Telenchana - Medicina Interna",
    },
    {
        image: "/assets/images/dr-toapanta.png",
        name: "Evelin Toapanta - Odontología",
    },
    {
        image: "/assets/images/dr-zuñiga.png",
        name: "Valeria Zuñiga - Medicina Interna",
    },
];

export const StatusIcon = {
    scheduled: "/assets/icons/check.svg",
    pending: "/assets/icons/pending.svg",
    cancelled: "/assets/icons/cancelled.svg",
};