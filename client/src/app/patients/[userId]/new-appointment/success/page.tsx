import { getAppointment } from '@/lib/actions/appointment.actions'
import Image from 'next/image'
import Link from 'next/link'
import React from 'react'
import { Doctors } from '../../../../../../constants'
import { formatDateTime } from '@/lib/utils'
import { Button } from '@/components/ui/button'

const Success = async ({ params: { userId }, searchParams }: SearchParamProps) => {
    const appointmentId = (searchParams?.appointmentId as string) || ''
    const appointment = await getAppointment(appointmentId)

    const doctor = Doctors.find((doc) => doc.name === appointment.primaryPhysician)

    return (
        <div className='flex h-screen max-h-screen px-[5%] '>
            <div className='success-img'>
                <Link href='/'>
                    <Image
                        src='/assets/icons/danymed.png'
                        width={3000}
                        height={3000}
                        alt='Logo'
                        className='h-40 w-fit'
                    />
                </Link>

                <section className='flex flex-col items-center'>
                    <Image
                        src='/assets/gifs/success.gif'
                        width={300}
                        height={280}
                        alt='Success'
                    />

                    <h2 className='header mb-6 max-w-[600px] text-center'>
                        Tú <span className='text-green-500'>agendamiento de cita</span> ha sido enviada exitosamente!
                    </h2>

                    <p>En unos momentos confirmaremos tu solicitud</p>
                </section>

                <section className='request-details'>
                    <p>Detalles de la cita solicitada:</p>

                    <div className='flex items-center gap-3'>
                        <Image
                            src={doctor?.image!}
                            alt='doctor'
                            width={100}
                            height={100}
                            className='size-6'
                        />

                        <p className='whitespace-nowrap'>Dr. {doctor?.name} </p>
                    </div>

                    <div className='flex gap-2'>
                        <Image
                            src='/assets/icons/calendar.svg'
                            width={24}
                            height={24}
                            alt='calendar'
                        />

                        <p>{formatDateTime(appointment.schedule).dateTime} </p>
                    </div>
                </section>

                <Button variant='outline' className='shad-priamry-btn' asChild>
                    <Link href={`/patients/${userId}/new-appointment`}>
                        Nueva Cita
                    </Link>
                </Button>

                <p className='copyright'>
                    © Todos los derechos reservados {new Date().getFullYear()}
                </p>
            </div>
        </div>
    )
}

export default Success
