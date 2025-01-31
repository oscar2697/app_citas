"use client"

import { zodResolver } from "@hookform/resolvers/zod"
import { useForm } from "react-hook-form"
import { z } from "zod"
import { Form } from "@/components/ui/form"
import CustomFormField from "../CustomFormField"
import SubmitButton from "../SubmitButton"
import { useState } from "react"
import { LoginFormValidation, UserFormValidation } from "@/lib/validation"
import { useRouter } from "next/navigation"
import "react-phone-number-input/style.css";
import { loginUser } from "@/lib/actions/patient.actions"

export enum FormFieldTypes {
    INPUT = 'input',
    PASSWORD = 'password',
}

export function LoginForm() {
    const router = useRouter()
    const [isLoading, setIsLoading] = useState(false)

    const form = useForm<z.infer<typeof LoginFormValidation>>({
        resolver: zodResolver(LoginFormValidation),
        defaultValues: {
            email: "",
            password: "",
        },
    })

    async function onSubmit({ email, password }: z.infer<typeof LoginFormValidation>) {
        setIsLoading(true)

        try {
            const userData = { email, password }
            const user = await loginUser(userData)

            if (user) {
                router.push(`/patients/${user.$id}/new-appointment`) 
            }
        } catch (error) {
            console.log(error)
        }

        setIsLoading(false)
        console.log(form)
    }

    return (
        <Form {...form}>
            <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-6 flex-1">
                <section className="mb-12 space-y-4">
                    <p className="text-dark-700">Ingresa tus datos para acceder a tu cuenta</p>
                </section>

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
                    fieldType={FormFieldTypes.PASSWORD}
                    control={form.control}
                    name="password"
                    label="Contraseña"
                    placeholder="••••••••"
                    iconSrc="/assets/icons/lock.svg"
                    iconAlt="password"
                />

                <SubmitButton isLoading={isLoading}>Ingresar</SubmitButton>
            </form>
        </Form>
    )
}
export default LoginForm
