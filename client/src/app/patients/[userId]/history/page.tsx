'use client'

import { useEffect, useState } from 'react'
import { getAppointmentsByUser } from '@/lib/actions/appointment.actions'
import { formatDateTime } from '@/lib/utils'

const AppointmentHistory = ({ userId }: { userId: string }) => {
    interface Appointment {
        $id: string;
        primaryPhysician: string;
        schedule: string;
        status: string;
    }

    const [appointments, setAppointments] = useState<Appointment[]>([])

    useEffect(() => {
        const fetchAppointments = async () => {
            const data = await getAppointmentsByUser(userId);
            setAppointments(data);
        }

        fetchAppointments(); 

        const interval = setInterval(() => {
            fetchAppointments();
        }, 3000);

        return () => clearInterval(interval); 
    }, [userId]);

    if (!appointments?.length) {
        return <p>No tienes citas registradas.</p>
    }

    return (
        <div className="p-12">
            <h2 className="text-xl font-bold mb-4">Historial de Citas</h2>
            <ul>
                {appointments.map((appointment) => (
                    <li key={appointment.$id} className="border p-8 rounded-lg shadow-md mb-3 bg-white">
                        <p className="text-gray-800">
                            <strong>Médico:</strong> Dr. {appointment?.primaryPhysician}
                        </p>
                        <p className="text-gray-800">
                            <strong>Fecha:</strong> {formatDateTime(appointment?.schedule).dateTime}
                        </p>
                        <p className="text-gray-800">
                            <strong>Estado:</strong> 
                            <span className={`ml-2 px-2 py-1 text-sm font-medium rounded-full ${
                                appointment.status === 'scheduled' ? 'bg-green-100 text-green-700' :
                                appointment.status === 'pending' ? 'bg-yellow-100 text-yellow-700' :
                                'bg-red-100 text-red-700'
                            }`}>
                                {appointment.status}
                            </span>
                        </p>
                    </li>
                ))}
            </ul>
        </div>
    )
}

export default AppointmentHistory
