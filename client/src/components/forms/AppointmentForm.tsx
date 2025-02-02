"use client"

import { zodResolver } from "@hookform/resolvers/zod"
import { useForm } from "react-hook-form"
import { z } from "zod"
import { Form } from "@/components/ui/form"
import CustomFormField from "../CustomFormField"
import SubmitButton from "../SubmitButton"
import { useState } from "react"
import { getAppointmentSchema } from "@/lib/validation"
import { useRouter } from "next/navigation"
import "react-phone-number-input/style.css";
import { FormFieldTypes } from "./PatientForm"
import { Doctors } from "../../../constants"
import { SelectItem } from "../ui/select"
import Image from "next/image"
import { createAppointment, updateAppointment } from "@/lib/actions/appointment.actions"
import { Appointment } from "../../../types/appwrite.types"

export function AppointmentForm({ userId, patientId, type = 'create', appointment, setOpen }: {
    userId: string
    patientId: string
    type: 'create' | 'schedule' | 'cancel'
    appointment?: Appointment
    setOpen?: (open: boolean) => void
}) {
    const router = useRouter()
    const [isLoading, setIsLoading] = useState(false)
    const AppointMentFormValidation = getAppointmentSchema(type)

    const form = useForm<z.infer<typeof AppointMentFormValidation>>({
        resolver: zodResolver(AppointMentFormValidation),
        defaultValues: {
            primaryPhysician: appointment ? appointment?.primaryPhysician : "",
            schedule: appointment
                ? new Date(appointment?.schedule!)
                : new Date(Date.now()),
            reason: appointment ? appointment.reason : "",
            note: appointment?.note || "",
            cancellationReason: appointment?.cancellationReason || '',
        },
    })

    async function onSubmit(values: z.infer<typeof AppointMentFormValidation>) {
        setIsLoading(true)
        let status

        switch (type) {
            case "schedule":
                status = "scheduled"
                break;
            case "cancel":
                status = "cancelled"
                break;
            default:
                status = "pending"
        }

        try {
            if (type === 'create' && patientId) {
                const appointmentData = {
                    userId,
                    patient: patientId,
                    primaryPhysician: values.primaryPhysician,
                    schedule: new Date(values.schedule),
                    reason: values.reason!,
                    note: values.note,
                    status: status as Status,
                }
                const appointment = await createAppointment(appointmentData)

                if (appointment) {
                    form.reset()
                    router.push(`/patients/${userId}/new-appointment/success?appointmentId=${appointment.$id}`)
                }
            } else {
                const appointmentToUpdate = {
                    userId,
                    appointmentId: appointment?.$id!,
                    appointment: {
                        primaryPhysician: values.primaryPhysician,
                        schedule: new Date(values.schedule),
                        status: status as Status,
                        cancellationReason: values.cancellationReason,
                    },
                    type,
                }

                const updatedAppointment = await updateAppointment(appointmentToUpdate);

                if (updatedAppointment) {
                    setOpen && setOpen(false);
                    form.reset();
                }
            }

        } catch (error) {
            console.log(error)
        }
        setIsLoading(false)
    }

    let buttonLabel

    switch (type) {
        case "cancel":
            buttonLabel = "Cancel Appointment";
            break;
        case "schedule":
            buttonLabel = "Schedule Appointment";
            break;
        default:
            buttonLabel = "Submit Apppointment";
    }

    return (
        <Form {...form}>
            <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-6 flex-1">
                {
                    type === 'create' &&
                    <section className="mb-12 space-y-4">
                        <h1 className="header">Nueva Cita</h1>
                        <p className="text-dark-700">Pide tu cita</p>
                    </section>
                }

                {type !== 'cancel' && (
                    <>
                        <CustomFormField
                            fieldType={FormFieldTypes.SELECT}
                            control={form.control}
                            name="primaryPhysician"
                            label="Doctor"
                            placeholder="Selecciona un doctor"
                        >
                            {Doctors.map((doctor) => (
                                <SelectItem key={doctor.name} value={doctor.name}>
                                    <div className="flex cursor-pointer items-center gap-2">
                                        <Image
                                            src={doctor.image}
                                            width={32}
                                            height={32}
                                            alt={doctor.name}
                                            className="rounded-full border border-dark-500 "
                                        />

                                        <p>{doctor.name}</p>
                                    </div>
                                </SelectItem>
                            ))}
                        </CustomFormField>

                        <CustomFormField
                            fieldType={FormFieldTypes.DATE_PICKER}
                            control={form.control}
                            name="schedule"
                            label="Date"
                            showTimeSelect
                            dateFormat="dd/MM/yyyy - h:mm aa"
                        />

                        <div className="flex flex-col gap-6 xl:flex-row">
                            <CustomFormField
                                fieldType={FormFieldTypes.TEXTAREA}
                                control={form.control}
                                name="reason"
                                label="Razón de la visita"
                                placeholder="Dinos la razón de tu visita"
                            />

                            <CustomFormField
                                fieldType={FormFieldTypes.TEXTAREA}
                                control={form.control}
                                name="note"
                                label="Comentarios o Notas"
                                placeholder="Tienes alguna nota o comentario?"
                                disabled={type === "schedule"}
                            />
                        </div>
                    </>
                )}

                {type == 'cancel' && (
                    <CustomFormField
                        fieldType={FormFieldTypes.TEXTAREA}
                        control={form.control}
                        name="cancellationReason"
                        label="Razón de la cancelación"
                        placeholder="Dinos la razón de la cancelación"
                    />
                )}

                <SubmitButton
                    isLoading={isLoading}
                    className={`${type === 'cancel' ? 'shad-danger-btn' : 'shad-primary-btn'} w-full`}
                >{buttonLabel}</SubmitButton>
            </form>
        </Form>
    )
}
export default AppointmentForm
