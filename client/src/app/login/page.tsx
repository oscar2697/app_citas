import LoginForm from "@/components/forms/LoginForm";
import Image from "next/image";
import Link from "next/link";

const LoginPage = () => {
    return (
        <div className="flex min-h-screen">
            <div className="w-1/2 flex flex-col justify-center items-center  text-white p-12">
                <div className="max-w-md w-full">
                    <div className="flex items-center gap-2 mb-8">
                        <Image
                            src='/assets/icons/danymed.png'
                            height={3000}
                            width={3000}
                            alt="Logo DanyMed"
                            className="mb-12 h-auto w-[300px] max-w-full"
                        />
                    </div>

                    <h2 className="text-3xl font-bold mb-2">¡Hola! 👋</h2>
                    <p className="text-gray-400 mb-6">Agenda tu cita</p>

                    <LoginForm />

                    <div className="mt-6 text-sm text-gray-400 text-center">
                        ¿No tienes cuenta? <Link href="/" className="text-green-400">Regístrate aquí</Link>
                    </div>
                </div>
            </div>

            <div className="w-1/2 relative hidden md:block">
                <Image
                    src="/assets/images/onboarding-img.png"
                    layout="fill"
                    objectFit="cover"
                    alt="Médicos"
                />
            </div>

            <footer className="absolute bottom-4 left-1/2 transform -translate-x-1/2 text-sm text-gray-400">
                © Todos los derechos reservados {new Date().getFullYear()}
            </footer>
        </div>
    );
};

export default LoginPage;