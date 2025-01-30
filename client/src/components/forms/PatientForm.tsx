"use client"

import { zodResolver } from "@hookform/resolvers/zod"
import { useForm } from "react-hook-form"
import { z } from "zod"
import { Form } from "@/components/ui/form"
import CustomFormField from "../CustomFormField"
import SubmitButton from "../SubmitButton"
import { useState } from "react"
import { UserFormValidation } from "@/lib/validation"
import { useRouter } from "next/navigation"
import { createUser } from "@/lib/actions/patient.actions"
import "react-phone-number-input/style.css";

export enum FormFieldTypes {
    INPUT = 'input',
    TEXTAREA = 'textarea',
    PHONE_INPUT = 'phoneInput',
    CHECKBOX = 'checkbox',
    DATE_PICKER = 'datePicker',
    SELECT = 'select',
    SKELETON = 'skeleton',
    PASSWORD = 'password',
}

export function PatientForm() {
    const router = useRouter()
    const [isLoading, setIsLoading] = useState(false)

    const form = useForm<z.infer<typeof UserFormValidation>>({
        resolver: zodResolver(UserFormValidation),
        defaultValues: {
            name: "",
            email: "",
            phone: "",
            password: "",
        },
    })

    async function onSubmit({ name, email, phone, password }: z.infer<typeof UserFormValidation>) {
        setIsLoading(true)

        try {
            const userData = { name, email, phone, password }
            const user = await createUser(userData)

            if (user) router.push(`/patients/${user.$id}/register`)
        } catch (error) {
            console.log(error)
        }
        setIsLoading(false)
    }

    return (
        <Form {...form}>
            <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-6 flex-1">
                <section className="mb-12 space-y-4">
                    <h1 className="header">Hola!👋🏻</h1>
                    <p className="text-dark-700">Agenda tu cita</p>
                </section>

                <CustomFormField
                    fieldType={FormFieldTypes.INPUT}
                    control={form.control}
                    name="name"
                    label="Nombre Completo"
                    placeholder="John Doe"
                    iconSrc="/assets/icons/user.svg"
                    iconAlt="user"
                />

                <CustomFormField
                    fieldType={FormFieldTypes.INPUT}
                    control={form.control}
                    name="email"
                    label="Email"
                    placeholder="example@email.com"
                    iconSrc="/assets/icons/email.svg"
                    iconAlt="email"
                />

                <CustomFormField
                    fieldType={FormFieldTypes.PHONE_INPUT}
                    control={form.control}
                    name="phone"
                    label="Número de Telefono"
                    placeholder="(099) 123 4567"
                />

                <CustomFormField
                    fieldType={FormFieldTypes.PASSWORD}
                    control={form.control}
                    name="password"
                    label="Contraseña"
                    placeholder="••••••••"
                    iconSrc="/assets/icons/lock.svg"
                    iconAlt="password"
                />

                <SubmitButton isLoading={isLoading}>Empezar</SubmitButton>
            </form>
        </Form>
    )
}
export default PatientForm
